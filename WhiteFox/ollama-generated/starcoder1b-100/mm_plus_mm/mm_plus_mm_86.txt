
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v = torch.mm(x1, x2)  # Matrix multiplication between input1 and input2
        v = v + 1   # Addition of the results of the two matrix multiplications
        return v


# Inputs to the model
input1 = torch.randn(2, 3, 64, 64)
input2 = torch.randn(2, 3, 64, 64)
