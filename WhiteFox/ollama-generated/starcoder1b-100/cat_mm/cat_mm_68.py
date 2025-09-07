
class Model(torch.nn.Module):
    def __init__(self, input_dim):
        super().__init__()
        self.conv = torch.nn.Conv2d(input_dim + 1, 8, 1, stride=1, padding=0)
 
    def forward(self, x1, x2):
        v1  = self.conv(torch.cat([x1, x1, ..., x1], dim=-1))
        v2 = torch.mm(v1, x2)
        return v2


# Initializing the model
m = Model(3 + 1)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 3, 3)
