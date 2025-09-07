
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + other
        return torch.relu(v2)


# Initializing the model and assigning another tensor to the variable `other` that is passed in as an argument of the `__init__` method
m, other = Model(), torch.randn(3, 8, 64, 64)

 # Inputs to the model 
 x1  = torch.randn(1, 3, 64, 64)
  __output__  = m(x1)
