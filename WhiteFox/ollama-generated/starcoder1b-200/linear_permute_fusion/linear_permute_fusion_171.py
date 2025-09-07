
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(...)

    def forward(self, x1):
        v1  = x1.permute(0, 2, 1)
        v2 = self.linear(...)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(...)  # A tensor whose dimensions are greater than two (such as a batch of 2 sequences).
