
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(128, 30)

    def forward(self, x1):
        v1 = self.linear(x1)
        return v1


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(5147963, 128) + 0.2

# Initializing the data for clamping operations
max_value = x1[:, :1].min().item() - 0.1

