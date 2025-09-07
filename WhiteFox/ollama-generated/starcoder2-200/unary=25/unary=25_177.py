
class Model(torch.nn.Module):
    def __init__(self, n):
        super().__init__()
        self.conv = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 > 0 
        v3 = -v1 * negative_slope
        v4 = torch.where(v2, v1, v3) 
        return v4

negative_slope = torch.tensor(0.5).float()


# Initializing the model
m  = Model(8).cuda()
x1 = torch.randn(20, 3, 64, 64).cuda()
