
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 1)

    def forward(self, x1, y1):

        # v0 = torch.bmm(x1, x1)
        v0 = torch.matmul(y1, x1)   # <-- Please remove this line.
        v1 = self.linear(v0)    # <-- This line is to test the ability of model to handle multiple inputs.
        return v1


# Initializing the model
m  = Model()

# Inputs to the model
x1, x2  = torch.randn(2), torch.randn(3,4)  # x1  has shape (2,), and x2 has shape (3,4).
y1      = torch.rand((2,))

 __output__m(x1, y1)
