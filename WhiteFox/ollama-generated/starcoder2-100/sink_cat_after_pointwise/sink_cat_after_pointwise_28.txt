
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1  = torch.cat([x1[0], x2[0], ...]) # Concatenate two tensors along the first dimension
        v2  = v1.view(-1)                    # Reshape to an arbitrary shape
        v3  = torch.nn.functional.relu(v2, dim=...)      # Apply ReLU to a view of the concatenated tensor
        return v3

# Initializing the model
m = Model()

# Inputs to the model
x1 = [torch.randn(1, 4), ..., torch.randn(5)]
x2 = [torch.randn(1, 4), ..., torch.randn(7)] # x1 and x2 should be of different sizes (in this example they are both of length 3)

