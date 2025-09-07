
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.mm(x1[0], x1[1])
        v2  = torch.cat([v1] * len(x1), dim=3)
        return v2


# Initializing the model
m = Model()

 # Inputs to the model