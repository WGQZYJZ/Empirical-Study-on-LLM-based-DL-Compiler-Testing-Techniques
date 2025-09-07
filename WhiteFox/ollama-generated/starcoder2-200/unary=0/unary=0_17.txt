
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 * 0.5
        v3  = v1 ** 2
        v4  = v3 ** v1 
        v5  = torch.log(v4 + 1e-7)/math.log(2) 
        return v2 * v5

# Initializing the model
m = Model()

