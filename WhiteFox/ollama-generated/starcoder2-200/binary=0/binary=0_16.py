
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, other):
        v1  = self.conv(x1)
        v2  = v1 + other
        return v2


# Initializing the model with an additional argument to the addition operation: "other" is a randomly generated 3-channel tensor.
m  = Model()
x1,  x2  = torch.randn(1, 3, 64, 64),torch.randn(1, 8, 50, 50)

 # Inputs to the model: "other" is a randomly generated 3-channel tensor
x1 = torch.randn(1, 3, 64, 64)
 
 # Initializing the model and feeding it inputs that contains two tensors: x1 and x2 
 m  = Model()
    x1,   other,  __output__  =  torch.randn(1, 8, 50, 50),torch.randn(1,3,64, 64),m(x1,other)