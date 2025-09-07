
class Model(torch.nn.Module):
    def __init__(self, input1, input2, input3, input4):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.mm(input1, input2)
        v2  = torch.mm(input3, input4)
        v3  = v1 + v2 
        return v3

# Initializing the model
m  = Model(x1, x1, x1, x1)

 # Inputs to the model
x1 = torch.randn(60, 50)
x2 = torch.randn(50, 49)
 
__output__= m(x1, x2, x1, x2)

