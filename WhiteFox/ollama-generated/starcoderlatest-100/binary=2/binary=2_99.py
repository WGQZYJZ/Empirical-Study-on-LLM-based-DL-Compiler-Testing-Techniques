
class Model(torch.nn.Module):
    def __init__(self, other: torch.Tensor = None):
        super().__init__()
        if isinstance(other, torch.Tensor):
            self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
            self.conv2 = torch.nn.Conv2d(8, 64, 1, stride=1, padding=1)
        else: # other is scalar.
            self.other = other
 
    def forward(self, x1):
        if isinstance(self.other, torch.Tensor):
            v1 = self.conv1(x1)
            v2 = v1 - self.other
        else: # self.other is scalar.
            v1 = self.conv2(x1)
            v2 = v1 - self.other * x1
        return v2


# Initializing the model with other tensor
m = Model() 
m = Model(other=torch.ones(64, 3)) 

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
