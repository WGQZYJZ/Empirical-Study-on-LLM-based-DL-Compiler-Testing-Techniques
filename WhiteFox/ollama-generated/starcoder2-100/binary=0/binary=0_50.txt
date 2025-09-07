
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, other):
        v2 = self.conv(x1) + other # 2nd tensor is passed as a keyword argument to the addition operation
        return v2


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(3,8,64,64)
other  = torch.randn(3,8,64,64)
__output__  = m(x1, other=other)

