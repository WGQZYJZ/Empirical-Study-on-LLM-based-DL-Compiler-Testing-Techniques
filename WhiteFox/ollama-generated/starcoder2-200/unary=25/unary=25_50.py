
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Linear(8, 1)
 
    def forward(self, x2):
        v0  = self.conv(x2)
        v1  = v0 > 0
        v3  = negative_slope 
        v4  = v0 * v3
        v5  = torch.where(v1, v0, v4)
        return v5


# Initializing the model