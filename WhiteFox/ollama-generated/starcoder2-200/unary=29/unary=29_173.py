
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
       v1 = convT(x1)
       v2 = torch.clamp_min(v1, minval)
       v3 = torch.clamp_max(v2, maxval)
# Inputs to the model
x1  = torch.randn(10, 64, 8, 8)
m(__output__) = m(x1)

