
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 1)

    def forward(self, x2):
        v1  = torch.nn.functional.linear(x2, self.linear.weight, self.linear.bias) # Apply linear transformation to the input tensor.
        v2  = v1.permute(-1, -3, -4)                                            # Permute the output tensor from the linear function.
        return v2


# Initializing the model