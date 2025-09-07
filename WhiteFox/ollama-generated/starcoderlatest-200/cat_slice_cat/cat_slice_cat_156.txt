
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.cat_0 = torch.nn.Cat(dim=1)
 
    def forward(self, x1):
        v1 = torch.cat([x1, 2**64*x1], dim=1)
        v2 = self.cat_0(v1, 3)
        return v2


# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
