import json
import os
import shutil
from deepface import DeepFace
from deepface.extendedmodels import Age, Gender, Race, Emotion

def face_recogn(img_path):


    result = DeepFace.find(img_path=img_path, db_path='face_check', enforce_detection=False, model_name='Facenet')
    result = result.values.tolist()
    return result, img_path



def check_file(result, img_path):
    if len(result):
        for i in result:
            file_name = i[0].split('/')[-1].split('.')[0]
            os.path.exists(f'faces/{file_name}')
            print(file_name)
            print('Папка найдена')
            destination = f"faces/{file_name}"
            dest = shutil.move(img_path, destination)
            print(f"Файл добавлен, путь{dest}")
            delete()
    else:
        analize(img_path)


def analize(img_path):
    file_name = img_path.split('/')[-1].split('.')[0]
    os.mkdir(f'faces/{file_name}')
    print(f'Папка создана {file_name}')
    result_dict = DeepFace.analyze(img_path=img_path, actions=('age', 'gender'), enforce_detection=False)
    total = {"age": result_dict.get("age"), "gender": result_dict.get("gender")}
    with open(f"faces/{file_name}/{file_name}.txt", "w", encoding="utf-8")as file:
        for key, val in total.items():
            file.write('{}:{}\n'.format(key, val))
    shutil.copy(img_path, "face_check")
    os.path.exists(f'faces/{file_name}')
    destination = f"faces/{file_name}"
    dest = shutil.move(img_path, destination)
    print(f"Файл добавлен, путь{dest}")
    delete()

def delete():
    for file in os.listdir("face_check"):
        if ".pkl" in file:
            os.remove(f"face_check/{file}")
    print("success")



if __name__ == '__main__':
    result, img_path = face_recogn(img_path='face_send/harry.jpeg')
    check_file(result, img_path=img_path)


