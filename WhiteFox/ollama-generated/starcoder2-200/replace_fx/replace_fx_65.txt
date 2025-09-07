
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2 = torch.rand_like(x1)  # Generate a random tensor of the same size as input_tensor and overwrite the old one
        v3 = torch.nn.functional.linear(v2, self.linear.weight, self.linear.bias)  # Apply linear transformation to this tensor. 
        return v3


# Initializing the model