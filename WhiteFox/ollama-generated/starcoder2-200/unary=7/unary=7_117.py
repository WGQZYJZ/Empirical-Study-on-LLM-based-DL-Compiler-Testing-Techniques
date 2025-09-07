class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 512)
        self.conv   = torch.nn.Conv2d(8, 64, 7, stride=2, padding=3)
 
    def forward(self, x1):
        l0 = self.linear(x1)
        v1 = l0 * clamp(min=0, max=l0 + 3) / 6

        return v1
