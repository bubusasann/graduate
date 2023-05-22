import pvcobra
import soundfile as sf
import os

access_key = "dd"  # Picovoice Console에서 가져온 AccessKey를 입력하세요
handle = pvcobra.create(access_key=access_key)
folder_path = 'C:\\Users\\user.DESKTOP-PS9S14D\\Desktop\\dev-clean\\LibriSpeech'  # 음성 파일들이 있는 폴더 경로


def get_next_audio_frame():
    pass  # 실제로 오디오 프레임을 반환하는 로직을 구현해야 합니다.


for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith(".wav"):
            audio_file_path = os.path.join(root, file)
            print(f"Processing file: {audio_file_path}")

            data, samplerate = sf.read(audio_file_path)
            handle.process(data)

            # 이제 여기에 결과를 처리하는 코드를 추가합니다.
            results = handle.get_inference_results()
            for result in results:
                audio_file = result['audio_file']
                voice_probability = result['voice_probability']

                if voice_probability > 0.5:
                    print(f"음성이 감지되었습니다. 파일: {audio_file}, 음성 확률: {voice_probability}")
                    # 음성이 감지되었을 때 수행할 작업 추가
                else:
                    print(f"음성이 감지되지 않았습니다. 파일: {audio_file}, 음성 확률: {voice_probability}")
                    # 음성이 감지되지 않았을 때 수행할 작업 추가

handle.delete()
