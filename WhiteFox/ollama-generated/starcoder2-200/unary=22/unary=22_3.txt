
class Model(torch.nn.Module):
    def __init__(self, size=4096, size1=5376, size2=8, size3=4):
        super().__init__()
        self.linear  = torch.nn.Linear(size1, size)
        self.tanh = torch.nn.Tanh()
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = self.tanh(v1)
        return v2


# Initializing the model
m  = Model(4096, 5376, 8, 4)

# Inputs to the model
x1  = torch.randn(size=(1, size=5376))
__output__  = m(x1)

