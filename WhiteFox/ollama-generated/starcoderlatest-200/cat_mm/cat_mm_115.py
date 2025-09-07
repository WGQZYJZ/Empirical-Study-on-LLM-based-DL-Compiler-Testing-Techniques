
class Model(torch.nn.Module):
    def __init__(self, dims):
        super().__init__()
        self.conv = torch.nn.Conv2d(dims[0], 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        return v6
 
# Input tensor to the model
x1 = torch.randn(1, dims[0], 64, 64)


