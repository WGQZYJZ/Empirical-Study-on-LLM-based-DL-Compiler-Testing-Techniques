
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, self.linear)  # Apply linear transformation to the input tensor.
        v2 = v1.permute(0, -1, -2) # Permute the output from linear transformation and swap the last two dimensions of this output.
        return v2


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(4, 3, 5)
