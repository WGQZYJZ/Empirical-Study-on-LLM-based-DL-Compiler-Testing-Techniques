
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        if other == None:
            self.lin = torch.nn.Linear(32, 64)
        else:
            self.lin = torch.nn.Linear(32, 64)

    def forward(self, x1):
        v1 = self.lin(x1) + other # Add another tensor to the output of the linear transformation
        return v1


# Initializing the model with a value for "other" as an input tensor that is not None
m = Model()
v2 = m(x1)

