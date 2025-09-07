
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        t1 = x1.permute(0, 2, 1)
        t2 = torch.cat([t1, t1], dim=1)  # Concatenate two tensors along a dimension
        v2 = self.linear(t2).view(-1)  # Reshape the concatenated tensor
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 2)
