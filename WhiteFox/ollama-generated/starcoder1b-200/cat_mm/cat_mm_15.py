
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        x2 = torch.randn_like(x1)
        v  = torch.cat([x1, x1, ..., x1], dim=0)
        return v


# Initializing the model
m = Model()

