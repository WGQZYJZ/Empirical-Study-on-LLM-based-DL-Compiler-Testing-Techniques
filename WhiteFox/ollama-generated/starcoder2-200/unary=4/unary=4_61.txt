
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.nn.functional.linear(x1) 
        v2  = v1 * 0.5 
        v3  = v1 * 0.7071067811865476 
        v4  = torch.erf(v3) 
        v5  = v4 + 1
        v6  = v2 * v5
        return v6


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 8) 
 __output__  = m(x1)

# Outputs from the model
v7  = torch.nn.functional.linear(x2) * (t5 + t3 - 0.9045084965895682  )

# Model 1: Output 3
v7  = torch.nn.functional.linear(x2) * ((x2 + x1)  /   (t1 - v7 + t4) )

