
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.m = torch.nn.Conv2d(1, 1, 3)

    def forward(self, x1, x2):
        return self.m(x1 * 0.5 + x2)


# Initializing the model
model = Model()


# Inputs to the model
input1 = torch.randn(4, 1, 64, 64)
input2 = torch.randn(4, 3, 64, 64)
output = model(input1, input2)


