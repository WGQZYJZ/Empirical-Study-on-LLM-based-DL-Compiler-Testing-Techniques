
class Model(torch.nn.Module):
    def __init__(self, input_dim=10):
        super().__init__()
        self.weight = torch.rand([input_dim], requires_grad=True)

    def forward(self, x1):
        v1  = x1[0] # Get a single slice of the first dimension from x1 tensor.
        v2  = torch.cat((v1, self.weight), dim=1)  # Concatenate it with self.weight.
        v3  = v2.view(5, -1).transpose(0, 1)     # Reshape and transpose the concatenated tensor to 5 x n_dim.
        v4  = torch.relu(v3 + 5 * torch.ones([1]))    # Apply a pointwise unary operation (e.g., ReLU or Tanh).
        return v4

# Initializing the model
m  = Model()

# Inputs to the model