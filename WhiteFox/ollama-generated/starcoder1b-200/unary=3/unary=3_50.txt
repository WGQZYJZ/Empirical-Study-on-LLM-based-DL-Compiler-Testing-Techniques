
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = F.avg_pool2d(x1, kernel_size=(1,1)) * 0.5
        v2 = F.avg_pool2d(v1, kernel_size=(1,1)) * 0.7071067811865476
        v3 = torch.erf(v2)
        v4 = v3 + 1
        v5 = v2 * v4
        return F.avg_pool2d(v5, kernel_size=(1,1))


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
