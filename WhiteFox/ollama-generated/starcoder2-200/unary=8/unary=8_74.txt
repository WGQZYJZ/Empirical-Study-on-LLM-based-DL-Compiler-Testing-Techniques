
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = self.conv2dtranspose(x1)
        v2  = v1 + 3
        v3  = torch.clamp(v2, min=0, max=6)
        v4  = v1 * v3 
        v5  = v4 / 6
        return v5

# Initializing the model
m = Model()

