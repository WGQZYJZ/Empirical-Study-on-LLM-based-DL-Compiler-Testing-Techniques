
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, ...)
        v2 = v1.permute(..., ..., 1)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = ...  # Original tensor containing a linear transformation
