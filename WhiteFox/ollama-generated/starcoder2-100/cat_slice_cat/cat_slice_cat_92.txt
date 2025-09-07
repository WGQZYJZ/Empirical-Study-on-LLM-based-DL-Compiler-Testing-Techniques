
class Model(torch.nn.Module):
    def __init__(self, size: int):
        super().__init__()

    def forward(self, x):
        t = torch.cat([x[0], x[1][0:size]])
        return t


# Initializing the model
m  = Model(size)


# Inputs to the model
x1  = [torch.randn(2, size), (torch.rand(39086745, 1))] # Input tensors with sizes [2, 3] and [39086745, 1], respectively
__output__  = m(*x1)

