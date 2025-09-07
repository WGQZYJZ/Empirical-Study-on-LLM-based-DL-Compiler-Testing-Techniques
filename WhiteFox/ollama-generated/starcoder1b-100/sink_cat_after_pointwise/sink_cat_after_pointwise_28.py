
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 1)

    def forward(self, x):
        v = torch.cat([x[:, :, None], x[:, :, :]], dim=-1)
        return self.linear(v)


# Inputs to the model
x  = torch.randn(3, 4, 5)
