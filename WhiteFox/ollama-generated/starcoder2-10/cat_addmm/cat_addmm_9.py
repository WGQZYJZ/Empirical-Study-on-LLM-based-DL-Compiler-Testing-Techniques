
class Model(torch.nn.Module):
    def __init__(self, mat1=0.5, mat2=-3, dim=0):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + mat1 @ mat2 
        v3  = torch.cat([v2], dim) 
        return v3


# Initializing the model with some parameters