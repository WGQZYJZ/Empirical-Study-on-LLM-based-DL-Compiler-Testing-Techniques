
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.25):
        super().__init__()
        self.linear = torch.nn.Linear(3 * 64 * 64, 1)
 
    def forward(self, x1):
        v1 = self.linear(x1.view(-1)) # Apply a linear transformation to the flattened input tensor. The shape of this tensor is (-1, 3 * 64 * 64), where -1 indicates that each row of this matrix will have the same number of elements.
        v2 = (v1 > 0).float() # Create a boolean tensor where each element is True if the corresponding element in t1 is greater than 0, and False otherwise. The output shape is (-1,) or (-1) depending on whether there's only one row.
        v3 = torch.relu(v2) * negative_slope + (torch.relu(-v2)).neg() # Multiply each element of the boolean tensor by the negative slope. For True elements, this will be 0. Otherwise, it will be -negative_slope.
        return torch.where(v1 > 0, v3, v4)


# Initializing the model
m = Model(0.25)


# Inputs to the model
x1  = torch.randn(1, 3 * 64* 64 )
