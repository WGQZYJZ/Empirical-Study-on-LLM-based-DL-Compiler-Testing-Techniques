
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 * 0.5 
        v3  = (v1 * v1).type(torch.double) # Cast to double precision for the multiplication
        v4  = ((v3 * v3) / 16.).type(torch.float)
        v5  = torch.mul(v2, v4)
        return v5


# Initializing the model