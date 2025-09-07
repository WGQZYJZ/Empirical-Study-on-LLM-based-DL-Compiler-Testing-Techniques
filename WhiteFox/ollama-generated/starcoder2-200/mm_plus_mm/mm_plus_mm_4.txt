
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1, input2):
        v1 = torch.mm(input1, input2) 
        v2 = torch.mm(input3, input4)  
        v3  = v1 + v2
        return v3


# Initializing the model
m  = Model()
x1 = torch.randn(8, 500) # Input tensor for the first matrix multiplication
x2 = torch.randn(600, 754) # Input tensor for the second matrix multiplication
 
__output__  = m(x1, x2)


