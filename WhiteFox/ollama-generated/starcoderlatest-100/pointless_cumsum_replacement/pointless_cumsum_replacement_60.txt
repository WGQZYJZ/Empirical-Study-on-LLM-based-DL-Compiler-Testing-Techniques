
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = torch.full([x1.shape[0], x1.shape[2]], 1, dtype=torch.float, layout=torch.strided, device='cuda:0', pin_memory=True)
        v2 = self.conv(x1)
        return v6


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
