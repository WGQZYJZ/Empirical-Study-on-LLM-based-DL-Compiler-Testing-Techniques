
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.view(-1, 2).permute(0, 2, 1)
        return torch.relu(v1 @ self.linear.weight + self.linear.bias)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 4)
