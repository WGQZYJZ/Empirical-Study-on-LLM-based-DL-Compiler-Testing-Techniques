
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        t1 = torch.cat([x1, x2], dim=0) # Concatenate the input tensors with 0 dimension

        v1 = t1.view(-1, 1, 2) # Reshape the concatenated tensor
        v2 = self.linear(v1) # Apply a pointwise unary operation (e.g., ReLU or Tanh) to the reshaped tensor
        return v2


# Inputs to the model
x1 = torch.randn(3, 2, 2)
