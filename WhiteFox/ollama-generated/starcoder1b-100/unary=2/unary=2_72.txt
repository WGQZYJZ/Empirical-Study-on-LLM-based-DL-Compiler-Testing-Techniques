
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2dTranspose(3, 8, 4, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = torch.abs(v2) ** 3
        v4 = torch.log(torch.sqrt(2.0)) / 2
        v5 = v3 + v4
        v6 = v1 * (torch.exp(v5) - 1)
        return v6


# Initializing the model
m = Model()


