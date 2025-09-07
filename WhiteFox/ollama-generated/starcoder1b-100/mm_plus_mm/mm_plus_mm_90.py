
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        t1 = torch.mm(x1, x2)  # Matrix multiplication between input1 and input2
        t2 = torch.mm(x3, x4)  # Matrix multiplication between input3 and input4
        return t1 + t2


# Inputs to the model
x1 = torch.randn(3, 64, 64)
x2 = torch.randn(4, 64, 64)
