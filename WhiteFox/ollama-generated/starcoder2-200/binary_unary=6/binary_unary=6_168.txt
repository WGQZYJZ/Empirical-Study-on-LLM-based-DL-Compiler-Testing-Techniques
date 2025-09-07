
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 5)

    def forward(self, x):

        v1  = 2 * x
        v2 = self.linear(v1)
        v3  = other
        return (v2 - v3), relu((v2 - v3))


# Initializing the model with initial values and outputs
m = Model()
other = torch.rand([5]) # Replace with the output of the previous model
__output__, _ = m(torch.rand([10]))