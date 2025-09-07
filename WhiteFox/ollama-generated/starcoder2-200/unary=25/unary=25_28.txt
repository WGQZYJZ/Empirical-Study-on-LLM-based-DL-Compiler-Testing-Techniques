
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
       v1 = torch.nn.functional.linear(x1)
       v2  = (v1 > 0).to(dtype=int)
       negative_slope = -3 
       v3 = v1 * negative_slope
       v4 = torch.where(v2 == 1, v1, v3)
       return v4


# Initializing the model