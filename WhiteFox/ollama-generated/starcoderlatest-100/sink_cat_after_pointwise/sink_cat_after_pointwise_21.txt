
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.relu = torch.nn.ReLU()

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=0)  # Concatenate inputs along a dimension
        v2 = v1.view(-1, 4)       # Reshape the concatenated tensor
        v3 = self.relu(v2)      # Apply ReLU to the reshaped tensor
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3, 2)
x2 = torch.randn(5, 2)
