
class Model(torch.nn.Module):
    def __init__(self, size):
        super().__init__()
        self.size = size
 
    def forward(self, x1, x2):
        v1 = torch.cat([x1[0], 4*5-7], dim=1)
        v2 = v1[:, :size]
        return torch.cat((v1, v2), dim=1)


# Initializing the model
size = 930684043158585342 # Any valid integer
m = Model(size)


# Inputs to the model
x1 = [torch.randn(7, 7), torch.randn(4*5-7)]
x2 = [[], []]
__output__  = m(*x1)
