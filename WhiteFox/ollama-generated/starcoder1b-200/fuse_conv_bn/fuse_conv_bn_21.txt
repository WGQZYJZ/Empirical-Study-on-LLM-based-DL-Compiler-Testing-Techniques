
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(...)

    def forward(self, x1):
        v1 = ...  # ConvXd input
        v2 = ...  # BatchNormXd input
        v3 = ...  # Linear input

        return torch.relu(self.linear(v1))


# Initializing the model
m = Model()


