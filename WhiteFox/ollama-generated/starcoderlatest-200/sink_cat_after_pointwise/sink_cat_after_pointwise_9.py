
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 1)

    def forward(self, x1, x2):
        t1 = torch.cat([x1, x2], dim=0) # Concatenate input tensors along the first dimension (axis=0), and reshape the concatenated tensor.
        t2 = t1.view(-1, 2)       # The shape of this reshaped tensor should be [4, 2].
        t3 = torch.relu(t2)         # This is a pointwise unary operation (e.g., ReLU or Tanh).
        return self.linear(t3)

# Initializing the model
m = Model()
x1 = torch.randn(4, 2, requires_grad=True)
x2 = torch.randn(4, 2, requires_grad=True)
