
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 8)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        return v1
 

# Initializing the model
m = Model()


# Inputs to the model
other = torch.randn(4096).requires_grad_()
x1   = torch.randn(32, 32) + other
__output__  = m(x1) 

