
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.Dropout(0.2)

    def forward(self, x1):
        v1 = torch.rand_like(x1)
        return self.dropout(v1)

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 2)
