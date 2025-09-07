
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2, x3, x4):
        v1  = torch.mm(x1, x2) 
        v2  = torch.mm(x3, x4)
        return v1 + v2


# Initializing the model
m  = Model()

# Inputs to the model
i1 = torch.randn(2, 64).cuda()
i2 = torch.randn(64, 8).cuda()
i3 = torch.randn(50, 64)
i4 = torch.randn(8, 90)
