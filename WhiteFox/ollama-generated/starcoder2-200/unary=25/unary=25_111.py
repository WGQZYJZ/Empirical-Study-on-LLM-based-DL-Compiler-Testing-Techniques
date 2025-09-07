
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
       v1  = self.linear(x1) 
       v2 = torch.where(v1 > 0, v1, -v1 * negative_slope )
       return v2


# Initializing the model