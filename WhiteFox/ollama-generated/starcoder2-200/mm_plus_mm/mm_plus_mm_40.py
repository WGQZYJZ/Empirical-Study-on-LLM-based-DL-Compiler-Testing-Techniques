
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3, x4):
        v1 = torch.mm(x1, x2) # Matrix multiplication between input1 and input2
        v2  = torch.mm(x3, x4)  # Matrix multiplication between input3 and input4
        return v1 + v2


# Initializing the model
m  = Model()
__output__  = m(torch.randn(50),
                torch.randn(68, 79), 
                torch.randn(50, 50),  
                torch.randn(43, 50))
