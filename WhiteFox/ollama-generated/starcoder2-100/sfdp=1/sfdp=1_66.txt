
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8, 4)
        self.conv1  = torch.nn.Conv2d(3, 6, 5)

    def forward(self, x1):

        v0 = self.conv1(x1)
        v7 = v0 + 1 # This line introduces a new symbol
        v8 = self.linear(v7) # This line introduces a new symbol

        return v8


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 3, 500, 500)
