
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(64, 32)
        self.linear2 = torch.nn.Linear(32, 8)

    def forward(self, x1):
        v1 = self.linear1(x1)
        v2 = v1 + other  # Add another tensor to the output of the linear transformation
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 64)
