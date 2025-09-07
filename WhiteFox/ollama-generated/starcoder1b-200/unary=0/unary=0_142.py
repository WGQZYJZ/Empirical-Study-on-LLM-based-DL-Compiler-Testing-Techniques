
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1).pow_(0.5)
        v2 = (v1 * (v1)).sqrt_()
        v3 = (v1 * v1).pow_(0.044715)
        v4 = v3 * v1
        v5 = v4 + 1
        v6 = v2 * v5
        return v6


# Initializing the model
m = Model()


