
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.bmm = torch.bmm

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.bmm(v1, x2)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3, 4, 5, 6)  # Input tensor A
x2 = torch.randn(7, 8, 9, 10)  # Input tensor B
__output_A = m(x1, x2)  # Output from model with input (x1, x2)
__output_B = m(x2, x1)  # Output from model with input (x2, x1)


