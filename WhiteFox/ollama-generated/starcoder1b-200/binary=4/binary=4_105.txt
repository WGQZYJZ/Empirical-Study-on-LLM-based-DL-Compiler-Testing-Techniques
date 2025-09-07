
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(320, 40)

    def forward(self, x1):
        v1 = self.linear1(x1)
        return v1


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 320, dtype=torch.float, requires_grad=True)
