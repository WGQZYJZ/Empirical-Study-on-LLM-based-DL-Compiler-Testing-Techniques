
class Model(torch.nn.Module):
    def __init__(self, input1, input2, input3, input4):
        super().__init__()
 
    def forward(self, x1, y1):
        v0 = torch.mm(x1,  y1)
        v1 = torch.mm(input3, input4) 
        v2 = v0 + v1 
        return v2

# Initializing the model with random values for the inputs
input1  = torch.rand(5, 6)
input2  = torch.rand(6, 7)
 
input3  = torch.rand(8, 9)
input4  = torch.rand(9, 10)
m  = Model(input1, input2, input3, input4)

 # Inputs to the model
x1  = torch.randn(5, 6)
y1  = torch.randn(6, 7)
 
 __output__  = m(x1, y1).item()

