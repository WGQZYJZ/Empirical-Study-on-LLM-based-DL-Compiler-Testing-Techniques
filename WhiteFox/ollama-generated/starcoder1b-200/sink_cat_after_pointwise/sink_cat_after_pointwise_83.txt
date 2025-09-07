
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)  # Permute the input tensor
        t2 = v1.contiguous()
        t3 = torch.relu(t2)  # Apply a pointwise unary operation (e.g., ReLU or Tanh) to the permuted tensor
        return t3


# Inputs to the model
x1 = torch.randn(1, 2, 2)
