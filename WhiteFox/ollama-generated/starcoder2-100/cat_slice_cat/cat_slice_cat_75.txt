
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1[:, :, :9223372036854775807]) # Slice the concatenated tensor along dimension 1
        return torch.cat([x1, v1], dim=1)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(32, 3, 64, 64)
