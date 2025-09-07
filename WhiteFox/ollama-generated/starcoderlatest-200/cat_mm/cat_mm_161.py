
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, ... , xn):
        v1 = torch.mm(x1, input2)
        v2 = torch.cat([v1, v1, ..., v1], dim=0)
        return v6


# Initializing the model
m = Model()

