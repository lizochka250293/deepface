import json
import os
import shutil
from deepface import DeepFace
from deepface.extendedmodels import Age, Gender, Race, Emotion

def face_recogn(img_path):
    try:
        result = DeepFace.find(img_path=img_path, db_path='face_check')
        result = result.values.tolist()

        check_file(result, img_path)

    except Exception as _ex:
        return _ex

def check_file(result, img_path):
    if len(result) > 0:
        for i in result:
            file_name = i[0].split('/')[-1].split('.')[0]
            os.path.exists(f'{file_name}')
            print(file_name)
            print('Папка найдена')
            destination = f"{file_name}"
            dest = shutil.move(img_path, destination)
            print(f"Файл добавлен, путь{dest}")
            delete()
    else:

        file_name = img_path.split('/')[-1].split('.')[0]
        os.mkdir(f'{file_name}')
        print(f'Папка создана {file_name}')
        destination = f"{file_name}"
        dest = shutil.move(img_path, destination)
        print(f"Файл добавлен, путь{dest}")
        delete()


def analize(img_path):
    file_name = img_path.split('/')[-1].split('.')[0]
    os.mkdir(f'{file_name}')
    print(f'Папка создана {file_name}')
    result_dict = DeepFace.analyze(img_path=img_path, actions=('age', 'gender'), enforce_detection=False)
    total = {"age": result_dict.get("age"), "gender": result_dict.get("gender")}
    with open(f"{file_name}/{file_name}.txt", "w", encoding="utf-8")as file:
        for key, val in total.items():
            file.write('{}:{}\n'.format(key, val))

def delete():
    if os.path.isfile(r'C:\Users\bt030\PycharmProjects\search_by_photo\face_check\representations_vgg_face.pkl'):
        os.remove(r'C:\Users\bt030\PycharmProjects\search_by_photo\face_check\representations_vgg_face.pkl')
        print("success")
    else: print("File doesn't exists!")


if __name__ == '__main__':
    # print(face_recogn(img_path='face_send/johnny-depp-8.jpg'))
    analize(img_path='face_send/johnny-depp-8.jpg')

