
class Model(torch.nn.Module):
    def __init__(self, size):
        super().__init__()
 
    def forward(self, x0):
        t1 = torch.cat([x0], dim=1)
        t2  = t1[:, :9223372036854775807] 
        t3 = t2 [: ,: size ] # Size is the parameter
        t4 = torch.cat( [t1, t3 ], dim=1 )
 
        return t4


# Initializing the model
m  = Model(size)


# Inputs to the model
x0  = [torch.randn(8,256),] * 9

