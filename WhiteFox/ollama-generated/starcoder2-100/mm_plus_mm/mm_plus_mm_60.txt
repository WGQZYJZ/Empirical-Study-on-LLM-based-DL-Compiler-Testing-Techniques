
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y1, x2, y2):
        v1 = torch.mm(x1, y1) # Matrix multiplication between input1 and input2
        v2 = torch.mm(y1, x2) # Matrix multiplication between input3 and input4
        v3  = v1 + v2 
        return v3


# Initializing the model
m  = Model()
 
 # Inputs to the model
x1  = torch.randn(10, 15)
y1  = torch.randn(15, 9)
x2  = torch.randn(8, 9)
__output__  = m(x1, y1, x2)

 