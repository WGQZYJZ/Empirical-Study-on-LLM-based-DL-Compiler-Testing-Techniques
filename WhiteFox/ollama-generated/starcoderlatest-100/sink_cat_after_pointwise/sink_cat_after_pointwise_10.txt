
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.cat([x1, x1], dim=0) # Concatenate the two tensors along the first dimension
        v2 = v1.view(v1.size(0), -1) # Reshape to a column vector
        v3 = torch.relu(v2) # Apply ReLU to the reshaped tensor
        return v3


# Initializing the model
m = Model()
# Inputs to the model
x1 = torch.randn(2, 2)
