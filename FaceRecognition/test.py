from deepface import DeepFace
import cv2
import matplotlib.pyplot as plt

#Now create one function to read and verify the images
def verify(img1_path,img2_path):
    img1= cv2.imread(img1_path)
    img2= cv2.imread(img2_path)
    
    plt.imshow(img1[:,:,::-1])
    plt.show()
    plt.imshow(img2[:,:,::-1])
    plt.show()
    output = DeepFace.verify(img1_path,img2_path)
    print(output)
    verification = output['verified']
    if verification:
       print('They are same')
    else:
       print('The are not same')

#verify('img1.jpg','img2.jpg')

img = cv2.imread('img3.jpg')
imgplot = plt.imshow(img)
obj = DeepFace.analyze(img_path = "img3.jpg", actions = ['age', 'gender', 'race', 'emotion'])
print(obj["age"]," years old ",obj["dominant_race"]," ",obj["dominant_emotion"]," ", obj["gender"])