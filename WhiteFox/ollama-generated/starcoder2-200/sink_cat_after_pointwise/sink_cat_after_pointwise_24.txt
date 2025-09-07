
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.cat([x1, x2], dim=0)  # Concatenate tensors along a dimension
        v2 = v1.view(-1)  # Reshape the concatenated tensor
        v3 = torch.relu(v2)  # Apply a pointwise unary operation (e.g., ReLU or Tanh) to the reshaped tensor
        return v3

# Initializing the model
m  = Model()


# Inputs to the model: 1. Input for first concatenation of tensors along a dimension; 2. Input for the second one in the above mentioned pattern.
x1, x2 = torch.randn(10, 3), torch.randn(5, 3) # Tensor 1 has shape [batch_size] x [input_size]; tensor 2: [batch size] x [input size].
