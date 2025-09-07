
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 1)

    def forward(self, x0):
        v0 = x0.permute((0, 3, 1, 2))
        v1 = torch.bmm(v0[0], v0[1])
        return self.linear(v1).squeeze(-1)


# Initializing the model
m = Model()

# Inputs to the model
x0 = torch.randn(3, 4, 2, 5)
