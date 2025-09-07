
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.m = torch.nn.Linear(3, 1)

    def forward(self, x1, x2):
        return self.m(x1 * x2)


# Initializing the model
m = Model()

# Inputs to the model
input1 = torch.randn(10, 3)
input2 = torch.randn(10, 3)
