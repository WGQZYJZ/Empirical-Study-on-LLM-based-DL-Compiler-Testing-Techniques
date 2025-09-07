
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, self.linear.weight) # Apply linear transformation to the input tensor.
        v2  = v1.permute(-1, -3, -2) # Permute the output tensor from the linear function
        return v2

# Initializing the model