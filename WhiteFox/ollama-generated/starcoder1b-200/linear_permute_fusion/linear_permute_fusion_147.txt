
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 4)

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, 2, 2) # First apply linear transformation on input tensor
        return v1


# Inputs to the model
x1 = torch.randn(2, 3, 4)
