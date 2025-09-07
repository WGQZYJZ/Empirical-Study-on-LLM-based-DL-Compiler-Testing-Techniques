
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, self.linear.weight)  # Apply linear transformation to the input tensor 
        v2 = v1.permute(0, -1, 1) # Permute the output tensor of the linear function with more than 2 dimensions
        return v2


# Initializing the model