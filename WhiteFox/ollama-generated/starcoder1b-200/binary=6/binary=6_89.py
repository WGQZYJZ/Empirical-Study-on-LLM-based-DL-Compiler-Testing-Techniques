
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.linear = torch.nn.Linear(4, 2)

    def forward(self, x1):
        v1 = self.linear(x1) - torch.tensor([0.25]) # Subtract 0.25 from the output of the linear transformation
        return v1


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 4)
