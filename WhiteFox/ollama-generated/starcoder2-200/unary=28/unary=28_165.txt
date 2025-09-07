
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):

        # Initialization of the linear transformation.
        self.linear = torch.nn.Linear(25088, 4)
        self.linear.weight.data *= 3

        return 0


# Inputs to the model
x1 = torch.randn(729, 25088)

# Initializing the model
m = Model()

__output__  = m(x1)