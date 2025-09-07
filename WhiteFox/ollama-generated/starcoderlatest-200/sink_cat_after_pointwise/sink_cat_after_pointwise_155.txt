
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(4, 2)
        self.linear2 = torch.nn.Linear(2, 1)

    def forward(self, x):
        v1 = x.permute(0, 2, 3, 1).view(-1, 4) # Concatenate input tensor along the dim=2
        v2 = torch.relu(v1) # Apply a pointwise unary operation to concatenation
        return self.linear2(self.linear1(v2))


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(1, 4, 6, 3)
