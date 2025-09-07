
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 2)

    def forward(self, x1):
        v1 = torch.cat([x1[:, :, :-1], x1[:, :, 1:]], dim=-1)
        v2 = v1.view(-1, 6)
        return torch.relu(torch.matmul(v2, self.linear.weight) + self.linear.bias)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(10, 3, 4)
