
import torch 
from torch import nn
class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(3, 8, kernel_size=5) # kernel size is a tuple of integers (2D, 3D, and ND are supported)
        self.conv2 = nn.Conv2d(8, 64, 5)
        self.bn1 = nn.BatchNorm2d(num_features=8)
        self.relu  = nn.ReLU()
        self.maxpool1 = nn.MaxPool2d(kernel_size=(3,2))
        self.maxpool2 = nn.MaxPool2d(kernel_size=4)

    def forward(self, x):
        t1 = torch.nn.functional.relu(self.conv1(x)) 
        t1 =  self.bn1(t1) # batch normalization is the first layer after a convolution layer
        t3 = torch.nn.functional.relu(torch.nn.functional.conv2d(x, self.conv2.weight), inplace=False) 
        t4 = nn.MaxPool2d(kernel_size=(3, 2)) # maxpool is the first layer after a batch normalization layer
        t1  = torch.nn.functional.maxpool2d(t3, kernel_size=[5]) 
        t2 = self.relu(self.conv2(x))
        t4 = torch.nn.functional.maxpool2d(t2) # maxpool is the first layer after a convolutional layer
        return x


# Initializing the model
m  = Model()

