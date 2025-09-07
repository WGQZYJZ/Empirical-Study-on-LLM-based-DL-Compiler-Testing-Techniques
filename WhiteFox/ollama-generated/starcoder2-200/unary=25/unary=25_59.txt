
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32*32*8, 64)

    def forward(self, x1):
        v1 = self.linear(x1.view(-1, 32*32*8)) 
        v2 = (v1 > 0).type_as(v1)
        v3 = v1 * negative_slope # <output of linear transformation>
        v4 = torch.where(v2, v1, v3) 
        return v4


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(8*64, 3, 32, 32).cuda()
__output__  = m(x1)