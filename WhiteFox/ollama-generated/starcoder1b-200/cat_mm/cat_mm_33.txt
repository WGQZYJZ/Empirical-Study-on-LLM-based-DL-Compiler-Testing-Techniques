
class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = nn.Conv2d(3, 8, kernel_size=1)
 
    def forward(self, x1):
        v1 = torch.mm(x1, x1)
        v2 = [v1, v1, ..., v1]
        return torch.cat(v2, dim=0)


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
