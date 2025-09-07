
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        v0 = torch.cat([x1, x2], dim=3).view(-1, 64)
        return torch.nn.functional.tanh(v0 @ self.linear.weight + self.linear.bias)


# Initializing the model