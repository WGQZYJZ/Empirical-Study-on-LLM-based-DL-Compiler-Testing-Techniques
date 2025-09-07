
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(5 * 32 + 5760, 1)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.sigmoid(v1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3708, 5 * 32 + 5760) # 3708 is batch size here (not fixed in this exercise). Here, we use a random tensor as an example.
