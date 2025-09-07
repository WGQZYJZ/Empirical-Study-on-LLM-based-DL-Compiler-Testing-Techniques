
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mul = torch.nn.Linear(2, 1)
 
    def forward(self, x1, x2, x3, x4):
        v0  = torch.nn.functional.linear(x1, x2).to(torch.float)
        v1  = torch.mm(v0, x3.t()).to(torch.float)
        v2  = torch.mm(v1, x4).to(torch.float)
        return self.mul(v2[:,None])


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(320, 56789) # input tensor (of shape 320 x 56789). Use any of the public API functions for constructing 1D tensors here.
__output__  = m(x1, x1.clone(), x1, x1)

