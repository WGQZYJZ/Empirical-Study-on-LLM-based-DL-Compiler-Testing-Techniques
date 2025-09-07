
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.input1 = torch.randn(64, 64)
        self.input2 = torch.randn(32, 64)
 
    def forward(self, x1):
        t1 = torch.mm(x1, self.input2)
        t2 = torch.mm(self.input1, self.input2)
        return t1 + t2


# Inputs to the model
x1 = torch.randn(32, 64)
