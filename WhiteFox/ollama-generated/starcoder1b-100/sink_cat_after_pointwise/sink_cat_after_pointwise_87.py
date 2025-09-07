
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(3, 2)

    def forward(self, x1, x2=None):
        v1 = torch.cat([x1, x2], dim=-1)
        v2 = self.linear(v1).view(-1)
        return v2


# Inputs to the model
inputs = torch.randn(4, 3, 4)
outputs = Model()(inputs)
