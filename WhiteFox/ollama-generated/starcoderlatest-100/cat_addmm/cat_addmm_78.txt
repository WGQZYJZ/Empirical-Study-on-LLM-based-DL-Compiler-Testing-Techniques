
class Model(torch.nn.Module):
    def __init__(self, num_channels):
        super().__init__()
        self.conv = torch.nn.Conv2d(num_channels, 8, kernel_size=1)
 
    def forward(self, x):
        v1 = torch.addmm(x, mat1, mat2)
        v2 = torch.cat([v1], dim=dim)
        return v2
