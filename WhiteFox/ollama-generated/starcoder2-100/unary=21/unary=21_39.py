
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x):
        v1 = self.conv(x) 
        v2 = torch.tanh(v1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x  = torch.randn(4,3,64,64)
__output__  = m(x)
