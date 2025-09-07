
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 1)

    def forward(self, x1, x2):
        t1 = torch.cat([x1, x2], dim=0)
        t2 = t1.view(t1.size(0), -1) # Reshape the concatenated tensor
        t3 = torch.relu(t2) # Apply a pointwise unary operation (e.g., ReLU or Tanh) to the reshaped tensor
        return self.linear(t3)


# Initializing the model
m = Model()

x1 = torch.randn(3, 2, 2)
x2 = torch.randn(3, 2, 2)
