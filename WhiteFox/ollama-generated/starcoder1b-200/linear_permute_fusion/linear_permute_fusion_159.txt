
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(...)

    def forward(self, x1):
        return self.linear(x1).permute(..., ...)  # Permute the output tensor from the linear transformation.


# Inputs to the model
input_tensor = torch.randn(2, 3, 4)
