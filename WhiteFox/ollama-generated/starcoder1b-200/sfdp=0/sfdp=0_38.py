
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.tanh(v1) * 0.5
        v3 = v1 + 2
        v4 = (torch.tanh(v3) + 1) / 2
        v5 = v2 * v4
        v6 = torch.softmax(v5, dim=-1)
        return v6


# Initializing the model
m = Model()

