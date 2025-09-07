
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2=None):
        if x2 is None:
            v1  = x1.permute(0, 2, 1)
            v2  = torch.relu(self.linear(v1))
            return v2
        else:
            v1 = x1.permute(0, 2, 1).contiguous()
            v2 = self.linear(torch.cat([x1, x2], dim=-1))
            return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(3, 2, 4).contiguous()
