
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.linear = torch.nn.Linear(8, 50)

    def forward(self, x):
        v  = self.linear(x) + 3
        return torch.clamp_min(torch.clamp_max(v / 6, 0), 6)


# Initializing the model
m = Model()


