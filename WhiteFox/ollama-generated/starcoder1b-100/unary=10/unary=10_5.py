
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.linear = torch.nn.Linear(64 * 7 * 7, 50)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1 + 3, 0)
        v3 = torch.clamp_max(v2, 6)
        v4 = torch.div((v3 / 6), 6)
        v5 = self.linear(v4)
        return v5


# Initializing the model
m = Model()


