
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (v1 + 3).clamp_(0, 6)
        v3 = torch.clamp_min((v2 / 6), 1.7976931348623157e+308)
        v4 = torch.clamp_max(v3, -1.7976931348623157e+308)
        return (v1 * v4).round()

# Initializing the model
m = Model()


