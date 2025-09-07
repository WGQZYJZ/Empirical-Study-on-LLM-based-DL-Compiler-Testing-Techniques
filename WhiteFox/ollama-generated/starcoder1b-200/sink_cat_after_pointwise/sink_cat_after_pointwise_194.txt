
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2=None):
        t1 = torch.cat([x1, x2, ...], dim=1)  # Concatenate two tensors along a dimension
        return self.linear(t1)


# Initializing the model
m = Model()

