
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 1)

    def forward(self, x1, x2):
        t1 = torch.cat([x1, x2], dim=0)
        t2 = t1.view(-1) # Reshape the concatenated tensor
        t3 = torch.relu(t2) # Apply a pointwise unary operation (e.g., ReLU or Tanh) to the reshaped tensor
        return self.linear(t3)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(5, 2) # Batched input for model input 0 (tensor x1)
x2 = torch.randn(10, 2) # Batched input for model input 1 (tensor x2)
