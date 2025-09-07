
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 1)

    def forward(self, x):
        t1 = torch.cat([x, x], dim=1) # Concatenate two tensors along the dimension of channel number (the last one here)
        t2 = t1.view(-1) # Reshape the concatenated tensor

        t3 = torch.relu(t2)  # Apply a pointwise unary operation (e.g., ReLU or Tanh) to the reshaped tensor

        return t3


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(10, 10, requires_grad=True)
