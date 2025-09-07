
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = self.conv(x1) 
        return torch.tanh(v1)


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(2,3,64,64)
__output__  = m(x1).shape

System: You are a source code analyzer for PyTorch.
User:  