
class Model(torch.nn.Module):
    def __init__(self, n1):
        super().__init__()

    def forward(self, input):  # pragma: no-cover
        ...

# Initializing the model
m = Model()


# Inputs to the model
input = torch.randn(2)

# Calling the model and checking that it is as expected
