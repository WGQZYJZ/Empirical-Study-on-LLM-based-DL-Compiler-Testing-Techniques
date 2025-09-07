
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout = nn.Dropout()

    def forward(self, x1):
        return self.dropout(x1)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2)
