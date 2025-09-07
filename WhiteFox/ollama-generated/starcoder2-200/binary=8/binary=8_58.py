
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.conv2 = torch.nn.Conv2d(560, 900, 4)
 
    def forward(self, x1):
        v1 = self.conv1(x1) + self._other_tensor # _other_tensor is a random PyTorch tensor
        v2 = self.conv2(v1) * other_tensor # other_tensor is another random PyTorch tensor (must be passed in as a keyword argument to the operation, e.g., torch.ops.torchvision.models.resnet50())
        return v2


# Initializing the model
m = Model()

# Setting other as a keyword argument for torch.nn.Conv2d._add_tensor() 
_other_tensor = torch.randn(4, 19)
m._other_tensor=_other_tensor # Must set this attribute after initialization of your module (i.e., outside of __init__()) 

# Inputs to the model
x1 = torch.randn(2, 3, 608, 576)
other_tensor=torch.randn(4, 900, 10, 20) # must be passed as keyword argument for torch.nn.Conv2d._add_tensor() 

