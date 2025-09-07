

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(32, 64)
 
    def forward(self, x1):
        v0 = x1
        v1  = self.linear1(v0) # Apply a linear transformation to the input tensor specified by x1
        v2  = v1 + other # Add another tensor to the output of the linear transformation (specified by keyword argument "other")
        return v2


m  = Model()
x1  = torch.randn(32, 64)
x2  = torch.randn(32, 80)
__output__  = m(x1)(x2=x2) # Note that the second input tensor is specified by keyword argument "x2"

