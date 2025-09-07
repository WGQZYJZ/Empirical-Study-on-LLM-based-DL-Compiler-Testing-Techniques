
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2=None):
        if x2 is None:
            return torch.cat([x1], dim=-1)

        else:
            t = torch.cat([x1, x2], dim=0)  # Concatenate tensors along a dimension
            t = t.view(-1, 2)  # Reshape the concatenated tensor
            t = torch.relu(t)  # Apply a pointwise unary operation (e.g., ReLU or Tanh) to the reshaped tensor

            return t


# Initializing the model
m = Model()


