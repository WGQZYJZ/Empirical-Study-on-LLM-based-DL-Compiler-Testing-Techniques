
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        t1 = torch.cat([x1, x2], dim=-1)
        # Reshape and apply a pointwise unary operation
        t2 = t1.view(t1.size(0), -1)
        return self.relu(t2)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 3)
x2 = torch.randn(1, 2, 4)
