
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        t1 = torch.cat([x1, x2], dim=-1) # Concatenate tensor1 and tensor2 along dimension -1
        t2 = t1.view(t1.shape[0] * t1.shape[1])  # Reshape the concatenated tensor
        return torch.relu(t2) # Apply a pointwise unary operation (e.g., ReLU or Tanh) to the reshaped tensor

# Initializing the model
m = Model()


