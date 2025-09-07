
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 10)
        self.dropout = torch.nn.Dropout()

    def forward(self, x):
        return self.dropout(self.linear(x))


# Initializing the model
m = Model()
m.eval()

# Input to the model
x = torch.randn(10, 2, 5)
