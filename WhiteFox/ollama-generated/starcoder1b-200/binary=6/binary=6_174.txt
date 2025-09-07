
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(256, 128)

    def forward(self, x1):
        return self.linear(x1 - 0.01)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 256, requires_grad=True)
