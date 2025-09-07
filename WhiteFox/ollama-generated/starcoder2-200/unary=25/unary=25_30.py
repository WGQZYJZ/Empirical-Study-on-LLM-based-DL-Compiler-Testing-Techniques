
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = self.linear(x1) > 0
        v2 = v1 * -0.5

        # Leaky ReLU is implemented using torch.where() where the 3rd argument specifies what to choose for each element of v1 that corresponds to True in v2, and the 4th argument specifies what to choose otherwise.
        v3 = v2 + 1
        return self.linear(x1) * v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 60)
