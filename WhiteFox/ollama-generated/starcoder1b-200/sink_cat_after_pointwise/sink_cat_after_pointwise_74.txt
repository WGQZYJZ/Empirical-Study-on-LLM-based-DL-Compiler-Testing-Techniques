
class Model(torch.nn.Module):
    def __init__(self, hidden_dim=128):
        super().__init__()
        self.linear  = torch.nn.Linear(4, hidden_dim)

    def forward(self, x1):
        v1 = x1.view(-1, 4)
        return self.linear(v1)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(10, 3, 5).view(2, 5)  # Reshape `x1`
