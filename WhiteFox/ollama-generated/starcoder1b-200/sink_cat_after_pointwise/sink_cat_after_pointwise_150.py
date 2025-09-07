
class Model(torch.nn.Module):
    def __init__(self, hidden):
        super().__init__()
        self.hidden = hidden  # Store the hidden dimension

    def forward(self, x1):
        # Perform linear transformation on t1 (t2).
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.linear(v1, self.hidden, self.hidden)

        # Reshape and apply pointwise unary operation (ReLU or Tanh).
        v3 = t3.view(-1, self.hidden)
        return v3


# Inputs to the model
x1 = torch.randn(1, 2, 2)
