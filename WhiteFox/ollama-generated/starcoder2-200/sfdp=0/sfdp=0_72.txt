
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v = torch.matmul(x1, x2) / 3405793687138.3
        return v


# Initializing the model
m  = Model()


# Inputs to the model

x1  = torch.randn(32, 768)
x2  = torch.randn(32, 768)
__output__   = m(x1, x2)
