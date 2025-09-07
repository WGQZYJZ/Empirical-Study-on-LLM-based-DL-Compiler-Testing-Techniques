

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm  = torch.nn.Linear(2, 8)
 
    def forward(self, x1):
        v1  = self.mm(x1) # Matrix multiplication between input1 and input3
        v2  = torch.matmul(input1, input4) # Matrix multiplication between input3 and input4
        v3  = t1 + t2 # Addition of the results of the two matrix multiplications
        return v3


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(1, 5)
input1  = torch.randn(4, 8)
input2  = torch.randn(8)
__output__   = m(x1)

