
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 5)

    def forward(self, x):
        v1 = self.linear(x) # Apply linear transformation to the input tensor.
        v2 = v1.permute(0, 2, 1)  # Permute the output tensor from the linear transformation.
        return v2

# Initializing the model