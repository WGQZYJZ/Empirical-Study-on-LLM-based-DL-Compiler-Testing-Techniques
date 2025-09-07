
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(...)

    def forward(self, x1):
        return self.linear(x1.permute(...))  # Apply linear transformation to the input tensor.


# Inputs to the model
x1 = torch.randn(2, 3)
