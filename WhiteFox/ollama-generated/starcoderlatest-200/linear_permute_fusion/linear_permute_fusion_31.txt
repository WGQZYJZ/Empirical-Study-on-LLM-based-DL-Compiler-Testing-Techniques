
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 3)

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, 3 * [2]) # Apply linear transformation to the input tensor
        v2 = v1.permute(0, 2, 1) # Permute the output tensor from the linear transformation
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 2)
