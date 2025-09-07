
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        v2  = torch.cat([v1] * len([0]), 3)
        return v2


# Initializing the model and inputs to the model
m = Model()
x1  = torch.randn(16, 8, 4096).repeat(57, 1, 1) # repeat the tensor with 57 repetitions along dimension 0
x2  = torch.randn(3, 8, 4096)


__output__  = m(x1, x2)

