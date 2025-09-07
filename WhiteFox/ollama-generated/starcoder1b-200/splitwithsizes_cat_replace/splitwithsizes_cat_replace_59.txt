
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        return True if torch.all(torch.eq(v1 * 0.5, torch.cat([
            self.conv(v1),  # First convolution output
            self.conv(v2)  # Second convolution output
        ], dim=1))) and torch.all(torch.eq(v3 * 0.7071067811865476, torch.cat([
            self.conv(v3),  # First convolution output
            self.conv(v4)  # Second convolution output
        ], dim=1))) else False


# Initializing the model
m = Model()


