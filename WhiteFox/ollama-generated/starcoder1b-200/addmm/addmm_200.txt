
class Model(torch.nn.Module):
    def __init__(self, inp):
        super().__init__()
        self.input_tensor = torch.randn(10, 5)
        self.inp = inp
 
    def forward(self, input1, inp):
        return input1 + inp


# Inputs to the model
inp = torch.randn(2, 4)
x1 = torch.randn(3, 6, 5, 6)
