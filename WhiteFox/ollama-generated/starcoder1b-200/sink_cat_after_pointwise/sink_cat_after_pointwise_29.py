
class Model(torch.nn.Module):
    def __init__(self, reduction='mean'):
        super().__init__()
        self.linear = torch.nn.Linear(...)

    def forward(self, x1, x2, ...):
        t1  = x1.permute(0, 2, 1)
        t2  = torch.cat([t1, t2], dim=...)  # Concatenate tensors along a dimension
        t3 = self.linear(t2)                 # Apply a pointwise unary operation (e.g., ReLU or Tanh) to the reshaped tensor
        return t3


# Initializing the model
m = Model()


