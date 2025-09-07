
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8 * 64 ** 2, 10)

    def forward(self, x):
        y1 = torch.flatten(x)
        y3 = y1 + 1e-5 # added to the linear transformation output
        return self.linear(y3)

# Initializing the model
m = Model()

