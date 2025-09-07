
class Model(torch.nn.Module):
    def __init__(self, input1_dim):
        super().__init__()
        self.conv = torch.nn.Conv2d(input1_dim, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.cat([v1] * len(v1), dim=-1)
        return v2


# Initializing the model
m = Model(input1_dim=8)

# Inputs to the model
x1 = torch.randn(3, 64, 64)
