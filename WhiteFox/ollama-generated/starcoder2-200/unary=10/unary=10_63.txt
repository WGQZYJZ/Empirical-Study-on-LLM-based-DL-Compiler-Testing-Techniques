
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = self.linear(x1) # Linear transformation
        v2 = torch.clamp_min(v1 + 3, 0)  # Clamp the output of the addition operation to a minimum of 0 and then add 3
        v3  = torch.clamp_max(v2,6)# Clamp the output of the previous operation to a maximum of 6 
        v4  = v3 / 6 # Divide by 6 
        return v4


# Initializing model
m1 = Model()


# Input tensor x1
x1 = torch.randn(5)
__output__= m1(x1)