
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.linear = torch.nn.Linear(in_features=576, out_features=40)
 
    def forward(self, x):
        l1 = self.conv(x)
        l2 = l1 * clamp(min=0, max=6, l1 + 3)
        return l2 / 6


# Initializing the model
m = Model()


