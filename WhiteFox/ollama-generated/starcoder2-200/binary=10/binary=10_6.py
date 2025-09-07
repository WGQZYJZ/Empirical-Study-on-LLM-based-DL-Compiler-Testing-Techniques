
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2 = self.linear1(x1)
        v3 = torch.randn(v2.size()) + other
        return v3


# Initializing the model and setting the keyword argument "other" to a randomly generated tensor:
m  = Model()
other  = torch.randn(3, 50)

# Inputs to the model (without the keyword argument):
x1  = torch.randn(42768*3)
