
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1, input2, input3, input4):
        v1  = torch.mm(input1, input2)
        v2  = torch.mm(input3, input4) 
        v3  = v1 + v2
        return v3

m  = Model()

# Inputs to the model
x1  = torch.randn(5000, 6000)
x2  = torch.randn(6000, 7000)
x3  = torch.randn(4999, 8000)
x4  = torch.randn(8000, 15000)
__output__   = m(x1, x2, x3, x4)

