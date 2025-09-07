
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 1)

    def forward(self, x1):
        t1 = torch.cat([x1, x1], dim=0) # Concatenate a tensor along the first dimension
        t2 = t1.view(-1) # Reshape
        t3 = torch.relu(t2) # Apply a pointwise unary operation
        return self.linear(t3)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 4, 2)
