
class Model(torch.nn.Module):
    def __init__(self, dim=1024):
        super().__init__()
 
    def forward(self, x1, x2, x3, x4):
        v1  = torch.mm(x1, x2)
        v2  = torch.mm(x3, x4)
        return v1 + v2


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(1024, 512) # randomly generated matrix with dimensions of 1024 by 512
x2  = torch.randn(1024, 512) # randomly generated matrix with dimensions of 1024 by 512
x3  = torch.randn(768, 512)  # randomly generated matrix with dimensions of 768 by 512
x4  = torch.randn(768, 512)  # randomly generated matrix with dimensions of 768 by 512
__output__  = m(x1, x2, x3, x4).detach()

