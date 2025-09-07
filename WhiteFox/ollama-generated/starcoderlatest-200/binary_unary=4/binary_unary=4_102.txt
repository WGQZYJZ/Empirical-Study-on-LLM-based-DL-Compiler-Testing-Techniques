
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Linear(8192, 64)

    def forward(self, x1, x2=None):
        if x2 is None:
            v1 = F.relu(x1)
            v2 = v1 * 0.5
            return v2
        else:
            t1 = self.conv(torch.cat([x1, x2], dim=-1)) + x2 
            v3 = torch.nn.ReLU()(t1)
            return v3


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(8192, 4096, 1)
