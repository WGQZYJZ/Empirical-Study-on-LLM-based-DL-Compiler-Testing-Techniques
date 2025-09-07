
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.input1 = torch.rand(3, 64, 64)
        self.input2 = torch.randn(4, 8)
 
    def forward(self, x1, x2):
        y1 = torch.mm(x1, x2)
        y2 = t1 + t2
        return y1, y2


# Inputs to the model
x1 = torch.randn(3, 64, 64)
x2 = torch.randn(4, 8)
