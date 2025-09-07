
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2, x3, x4, x5, x6):
        m = torch.mm(x1, x2)  # Matrix multiplication between x1 and x2
        t = m + torch.mm(x3, x4)  # Matrix multiplication between x3 and x4
        return t


# Inputs to the model
x1  = torch.randn(2, 3, 64, 64)
x2  = torch.randn(2, 3, 128, 128)
x3  = torch.randn(2, 3, 128, 128)
x4  = torch.randn(2, 3, 64, 64)
x5  = torch.randn(2, 3, 64, 64)
x6  = torch.randn(2, 3, 128, 128)
