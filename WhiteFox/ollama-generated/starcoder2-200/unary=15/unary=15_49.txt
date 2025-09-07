
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.relu(self.conv(x1))
        return v2

 # Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)


|Model|
|:---:|
|class Model(torch.nn.Module):|
|def __init__(self):|
||super().__init__()|
|self.__conv__ = torch.nn.Conv2d(3,8,1)|
|def forward(self, x1):|
|v1 = self.__conv__(x1)|
|v2 = relu(v1) #Apply ReLU activation function to the output of the convolution|
|return v2|


|Inputs|
|:---:|
|x1 = torch.randn(1, 3, 64, 64)|

|Model output|
|:---:|
|`v1` is the output from the Conv layer.|