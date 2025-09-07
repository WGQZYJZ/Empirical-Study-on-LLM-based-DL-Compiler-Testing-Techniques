
class UpsampleThenLinear(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(64, 100, 3, stride=2, padding=1)
        self.linear = torch.nn.Linear(100, 10)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.sigmoid(v1)
        return self.linear(v2)


# Initializing the model
m = UpsampleThenLinear()


