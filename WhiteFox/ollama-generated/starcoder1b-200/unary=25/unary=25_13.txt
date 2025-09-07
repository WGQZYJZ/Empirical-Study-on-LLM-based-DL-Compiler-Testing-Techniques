
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 4)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        # Apply a linear transformation to the input tensor
        v2 = (v1 > 0).float()
        # Create a boolean tensor where each element is True if the corresponding element in t1 is greater than 0, and False otherwise
        v3 = v1 * negative_slope
        # Multiply the output of the linear transformation by the negative slope
        v4 = torch.where(v2, v1, v3)
        return v4


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 4, 64, 64)
