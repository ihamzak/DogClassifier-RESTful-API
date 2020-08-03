import io
import torch
import torchvision.transforms as transforms
from PIL import Image

from .classnames import breeds
from .model import model_transfer

def transform_image(image_bytes):
    my_transforms = transforms.Compose([transforms.Resize(224),
                                        transforms.CenterCrop(224),
                                        transforms.ToTensor(),
                                        transforms.Normalize(
                                            [0.485, 0.456, 0.406],
                                            [0.229, 0.224, 0.225])])
    image = Image.open(io.BytesIO(image_bytes))
    return my_transforms(image).unsqueeze(0)

model_transfer.eval()
# model_transfer.load_state_dict(torch.load('/Users/nomanikram/downloads/DogClassifier/model_transfer.pt'),map_location=torch.device('cpu'))
model_transfer.load_state_dict(torch.load('./Restful Api/module/model_transfer.pt', map_location=torch.device('cpu')))


def predict_breed_transfer(img_path):
    if ('.jpg' or '.jpeg' or '.png' in img_path) and img_path != None:
    # load the image and return the predicted breed
        image = Image.open(img_path).convert('RGB')
        prediction_transform = transforms.Compose([transforms.Resize(size=(224, 224)),
                                        transforms.ToTensor(),
                                        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])])

        # discard the transparent, alpha channel (that's the :3) and add the batch dimension
        image = prediction_transform(image)[:3,:,:].unsqueeze(0)
        # image = image.cuda()



        model_transfer.eval()
        idx = torch.argmax(model_transfer(image))
        return breeds[idx]
    return "Error"