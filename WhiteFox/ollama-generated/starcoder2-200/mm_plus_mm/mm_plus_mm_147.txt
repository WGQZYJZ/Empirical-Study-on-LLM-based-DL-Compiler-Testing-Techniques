
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm = torch.nn.Linear(1024, 3)
 
    def forward(self, x1, x2, x3, x4):
        v1  = torch.mm(x1, x2) # Matrix multiplication between input1 and input2
        v2  = torch.mm(x3, x4) # Matrix multiplication between input3 and input4
        v3  = v1 + v2 # Addition of the results of the two matrix multiplications
        return self.mm(v3)

# Initializing the model
m  = Model()


# Inputs to the model
input1  = torch.randn(50, 50).requires_grad_(True)
input2  = torch.randn(50, 784).requires_grad_(True) # Input for x1 50x784
input3  = torch.randn(50, 50).requires_grad_(True)
input4  = torch.randn(784, 3).requires_grad_(True) # Input for x2 784x3
 
__output__  = m(input1, input2, input3, input4)

