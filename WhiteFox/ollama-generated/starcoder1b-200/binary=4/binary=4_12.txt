
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 16)

    def forward(self, x1):
        v1 = self.linear(x1) + x1  # Add another tensor to the output of the linear transformation
        return v1


# Inputs to the model
x1 = torch.randn(32, 16)
