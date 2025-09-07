
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 1)

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=1) # Concatenate x1 and x2 along dimension 1
        v2 = v1.view(-1, self.linear.in_features) # Reshape the concatenated tensor into a vector. The resulting tensor has shape [batch_size*n_data, input_dimension].
        v3 = torch.relu(v2) # Apply a pointwise unary operation (e.g., ReLU or Tanh) to the reshaped tensor
        return self.linear(v3)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 2, 2)
x2 = torch.randn(4, 3, 2)
