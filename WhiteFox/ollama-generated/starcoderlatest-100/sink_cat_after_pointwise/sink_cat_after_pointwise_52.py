
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.relu = torch.nn.ReLU()

    def forward(self, t1):
        t2 = torch.cat([t1, t1], dim=2)  # Concatenate tensors along a dimension
        t3 = self.relu(t2)
        return t3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 4)
