
class Model(torch.nn.Module):
    def __init__(self, num_layers):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = torch.addmm(v1, x2, x2)
        v3 = torch.cat([v1], dim=1)
        return v3


# Initializing the model
m = Model(num_layers=2)


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
x2  = torch.randn(1, 8, 64, 64)
