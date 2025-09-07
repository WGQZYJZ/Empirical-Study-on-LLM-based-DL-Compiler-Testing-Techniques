
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x):
        v1 = self.conv(x)
        v2 = v1 * clamp(min=0, max=6, l1 + 3) / 6

# Initializing the model
m_new = Model2()

