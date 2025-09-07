
class Model(torch.nn.Module):
    def __init__(self, num_layers=3):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)
        for _ in range(num_layers):
            self.block = torch.nn.Sequential(*[
                nn.ReLU(),
            ])

    def forward(self, x1):
        return torch.relu(self.linear(x1))


# Initializing the model
m = Model()

