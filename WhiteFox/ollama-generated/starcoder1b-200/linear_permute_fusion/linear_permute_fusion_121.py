
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(...)

    def forward(self, x1):
        v1 = self.linear(...)  # The input to the linear function is v1 here.
        v2 = torch.nn.functional.linear(v1, ...)  # Apply the transformation to this tensor.
        return v2


# Initializing the model
m = Model()

