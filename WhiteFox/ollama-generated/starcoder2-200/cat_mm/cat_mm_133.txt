
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v0 = torch.cat([x1 + 15., x2 * (-3.)], 1) 
        return v0


# Initializing the model