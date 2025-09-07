
class Model(torch.nn.Module):
    def __init__(self, input_dim: int, output_dim: int):
        super().__init__()
        self.fc1 = torch.nn.Linear(input_dim, 32)
        self.fc2 = torch.nn.Linear(32, output_dim)

    def forward(self, x):
        x  = x.reshape(-1, 784)
        x  = F.relu(self.fc1(x))
        x  = self.fc2(x)
        return x


# Initializing the model
m = Model(3, 6)


# Inputs to the model
x  = torch.randn(10, 784)
