
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, y2):
        t = torch.mm(x1, y2) 
        return torch.cat([t] * 5 + [0])


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(32, 8) # The shape of tensor x1 is [32, 8], which represents a matrix multiplication result with eight columns and three matrices. The size of input1 is [32, 64]. 
y2 = torch.rand(8, 50)


