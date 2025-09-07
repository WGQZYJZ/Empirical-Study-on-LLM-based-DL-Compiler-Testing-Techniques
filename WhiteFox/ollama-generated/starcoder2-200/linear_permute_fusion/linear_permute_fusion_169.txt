
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 4)

    def forward(self, x):
        v1 = torch.nn.functional.linear(x, self.linear1.weight)
        v3 = v1.permute(0, -1, 1)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(2, 2)
