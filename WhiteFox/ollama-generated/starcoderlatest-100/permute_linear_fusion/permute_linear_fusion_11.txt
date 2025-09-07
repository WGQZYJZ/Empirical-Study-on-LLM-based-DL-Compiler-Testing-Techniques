
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 1)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1) # Add the permute operation in the model to simulate tensor methods in PyTorch
        return torch.nn.functional.relu(v1)

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 2)
