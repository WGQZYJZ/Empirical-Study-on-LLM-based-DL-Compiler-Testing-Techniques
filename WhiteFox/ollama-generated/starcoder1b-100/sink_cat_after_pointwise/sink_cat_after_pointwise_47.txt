
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 3)

    def forward(self, x1, x2=None):
        # The first `cat` operation is not detected in the model. Instead it comes before the reshaping `view`.
        v1 = torch.cat([x1, x2], dim=1)
        v2 = self.linear(v1)  # Apply a pointwise unary operation (e.g., ReLU or Tanh) to the concatenated tensor
        return v2


# Initializing the model
m = Model()


