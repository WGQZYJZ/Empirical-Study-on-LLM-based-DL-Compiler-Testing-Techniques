
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        v1 = x1.view(-1, 1)  # Reshape x1 with the shape [4, 2] to the shape [2, 4]
        v2 = torch.cat([v1, x2], dim=0)  # Concatenate v1 and x2 together with a new dimension of size 2
        v3 = self.linear(v2)  # Apply a pointwise unary operation (e.g., ReLU or Tanh) to the concatenated v2
        return v3


# Initializing the model
m = Model()


