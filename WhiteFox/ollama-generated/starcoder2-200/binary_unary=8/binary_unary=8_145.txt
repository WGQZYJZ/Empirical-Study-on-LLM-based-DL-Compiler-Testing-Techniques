
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + other # Other is a non-zero tensor of the same shape as v1 (this tensor should not be the output of another PyTorch API). We assume that v1 is not an input to this API.
        v3  = torch.relu(v2)
        return v3

# Initializing the model
m  = Model()
other  = torch.randn(8, 64, 64) # Any non-zero tensor of size (8, 64, 64).
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

