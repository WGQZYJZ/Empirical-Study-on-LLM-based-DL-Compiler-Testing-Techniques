
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 2)

    def forward(self, x1):
        v1 = torch.cat([x1] * 3, dim=-1).view(-1, x1.shape[-1])
        v2 = torch.relu(v1)
        return self.linear(v2)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(4, 2, 10)
