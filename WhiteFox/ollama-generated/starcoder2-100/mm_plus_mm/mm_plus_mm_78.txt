
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1, input2, input3, input4):
        v1  = torch.mm(input1, input2) # Matrix multiplication between input1 and input2
        v2  = torch.mm(input3, input4) # Matrix multiplication between input3 and input4
        v3  = v1 + v2                   # Addition of the results of the two matrix multiplications 
        return v3

# Initializing the model
m = Model()
__output__  = m(torch.randn(50, 6), torch.randn(50, 49), torch.randn(100, 78), torch.randn(20, 1))

