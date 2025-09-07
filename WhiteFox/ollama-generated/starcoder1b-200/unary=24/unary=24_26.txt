
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.where(v1 > 0, v1, v1 * 0.5)
        v3 = torch.where(v2 < 1, v1 / (1 + 0.7071067811865476 * abs(negative_slope)), t1)
        return v3

# Initializing the model
m = Model()


