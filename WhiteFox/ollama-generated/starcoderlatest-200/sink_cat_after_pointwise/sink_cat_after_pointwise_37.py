
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        t1 = torch.cat([x1, x1], dim=0)  # Concatenate two tensors along the dimension of 0
        t2 = t1.view(4)  # Reshape the concatenated tensor
        t3 = torch.relu(t2)  # Apply a pointwise unary operation to the reshaped tensor
        return t3

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 2, 2)
