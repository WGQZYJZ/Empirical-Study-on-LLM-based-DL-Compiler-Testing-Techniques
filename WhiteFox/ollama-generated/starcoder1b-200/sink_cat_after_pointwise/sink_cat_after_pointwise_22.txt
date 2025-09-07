
class Model(torch.nn.Module):
    def __init__(self, num_input_features=0):
        super().__init__()
        self.linear1 = torch.nn.Linear(num_input_features, 2)
        self.linear2 = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        v1  = torch.cat([x1, x2], dim=0) # Concatenate input tensors
        v2  = v1.view(-1, 4)            # Reshape the concatenated tensor
        v3  = self.linear1(v2)        # Apply linear transformation to the reshaped tensor
        v4  = torch.relu(self.linear2(v3)) # Apply pointwise unary operation (e.g., ReLU or Tanh) on the transformed tensor
        return v4


# Inputs to the model
x1, x2 = ...
