
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):  # Input tensor A and input tensor B must be permuted in the corresponding way.
        return torch.bmm(x1, x2)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(2, 2, 4)
