
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        m = (v1 > 0).long()
        v3 = v1 * negative_slope
        v4 = torch.where(m, v1, v3)
        return v4


# Initializing the model
m = Model()
