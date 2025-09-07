
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 1)

    def forward(self, x1):
        v1 = self.linear(x1) - 0.25 # Add another value 0.25 to the output of the linear transformation
        return torch.relu(v1)


# Initializing the model
m = Model()


