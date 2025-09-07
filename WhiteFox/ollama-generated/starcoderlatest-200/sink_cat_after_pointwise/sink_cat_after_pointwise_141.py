
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.relu = torch.nn.ReLU()

    def forward(self, x1, x2):
        t1 = torch.cat([x1, x2], dim=1)  # Concatenate the input tensors along a dimension
        t2 = t1.view(-1)  # Reshape the concatenated tensor
        t3 = self.relu(t2)  # Apply a pointwise unary operation (e.g., ReLU or Tanh) to the reshaped tensor
        return t3
