import sounddevice as sd
from google.cloud import texttospeech
import soundfile as sf
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file('service_account_credentials.json')
# Tạo client Text-to-Speech
client = texttospeech.TextToSpeechClient(credentials=credentials)

# Đường dẫn đến file readme.txt
input_file = "readme.txt"

# Đọc nội dung từ file
with open(input_file, "r") as file:
    text = file.read()

# Tạo input text
input_text = texttospeech.SynthesisInput(text=text)

# Thiết lập thông tin giọng nói
voice = texttospeech.VoiceSelectionParams(
    language_code="en-US",  # Ngôn ngữ và vùng miền của văn bản
    ssml_gender=texttospeech.SsmlVoiceGender.FEMALE  # Giới tính giọng nói
)

# Thiết lập định dạng âm thanh đầu ra
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.LINEAR16  # Sử dụng định dạng âm thanh WAV
)

# Gửi yêu cầu tạo âm thanh
response = client.synthesize_speech(
    input=input_text,
    voice=voice,
    audio_config=audio_config
)

# Lưu âm thanh thành file .wav
output_file = "output.wav"
with open(output_file, "wb") as file:
    file.write(response.audio_content)

print("Đã tạo file âm thanh:", output_file)


# Đọc file âm thanh
audio_data, sample_rate = sf.read(output_file)

# Chạy file âm thanh sử dụng sounddevice
sd.play(audio_data, sample_rate)
sd.wait()  # Đợi cho đến khi phát xong
