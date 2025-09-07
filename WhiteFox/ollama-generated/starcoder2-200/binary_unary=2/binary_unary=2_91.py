
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1) 
        return v1
 
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1) 
        return v1 * -1
 
class Model3(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = -0.5 * self.conv(x1) 
        return v1

# Initializing the model
m = Model()

 # Inputs to the model for initial model
x1_initial = torch.randn(1, 3, 64, 64)
 
 
 # Inputs to the model for a new model that will generate inputs to the model with a negative value scalar (scalar -1) in the pointwise convolution function output.
x2 = torch.randn(1, 3, 64, 64) * (-1.)

