
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(...)

    def forward(self, x1, x2, ...):
        v1 = x1.permute(...)  # Permute the input tensor
        v2 = torch.cat([v1, x2], dim=-1)  # Concatenate the tensors along a dimension
        v3 = torch.relu(v2)  # Apply a pointwise unary operation (e.g., ReLU or Tanh) to the reshaped tensor
        return v3


# Initializing the model
m = Model()


