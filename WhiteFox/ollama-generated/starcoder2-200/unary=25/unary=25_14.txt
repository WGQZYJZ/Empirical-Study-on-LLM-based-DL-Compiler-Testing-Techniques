
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.3):
        super().__init__()
        self.linear  = torch.nn.Linear(256 * 4 + 800 + 176*3+256, 4)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 > 0
        v3  = v1 * negative_slope
        v4  = torch.where(v2, v1, v3)
        return v4


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(50, 978 + 6 + 4 * (256 - 4))
__output__  = m(x1)