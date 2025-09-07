
class Model(torch.nn.Module):
    def __init__(self, other: torch.Tensor):
        super().__init__()
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + other
        v3  = torch.relu(v2)
        return v6

# Initializing the model and passing an argument as a keyword parameter to the constructor of the model class (model_class.__init__())
other: torch.Tensor = torch.randn()
m = Model(other=other):

 # Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
  __output__  = m(x1)