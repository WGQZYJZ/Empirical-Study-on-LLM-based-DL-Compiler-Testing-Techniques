
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - other

        return torch.relu(v2).to_numpy()


# Initializing the model
m  = Model()
other = 0 # Constant value that should be subtracted from the result of the linear transformation

# Inputs to the model
x1 = torch.randn(1, 3)

