
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.input1 = torch.randn(3, 64, 64)
        self.input2 = torch.randn(4, 64, 64)
        self.input3 = torch.randn(5, 64, 64)
 
    def forward(self):
        x = self.input1 + self.input2
        y = self.input3 + self.input4
        return torch.mm(x, y)


# Inputs to the model
x1  = torch.randn(3, 64, 64)
x2  = torch.randn(4, 64, 64)
