
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.input1 = torch.randn(3, 2, 5, 5)
        self.input2 = torch.randn(3, 2, 4, 4)
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        return v3


# Inputs to the model
x1 = torch.randn(3, 2, 5, 5)
x2 = torch.randn(3, 2, 4, 4)
