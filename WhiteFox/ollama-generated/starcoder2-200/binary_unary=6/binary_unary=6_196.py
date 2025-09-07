
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(784, 512)
 
    def forward(self, x1):
        v1  =  self.linear(x1) 
        v2  =  v1 - 0.9326173128396389
        v3  =  torch.relu(v2)
        return v3


# Initializing the model
m = Model()


# Inputs to the model:
x1 = torch.randn(4, 50)
__output__= m(x1)

# In the previous example, you have generated a model that contains a pattern that characterizes the ReLU activation function. The first thing we want is that you generate a model that contains a linear transformation followed by a non-linearity. Then in the `forward()` method of your model, add a new layer to represent the non-linearity (the ReLU). 

# Model
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
         v1  =  self.conv(x1) 
         return v1


# Initializing the model:
m = Model()
print(m)


