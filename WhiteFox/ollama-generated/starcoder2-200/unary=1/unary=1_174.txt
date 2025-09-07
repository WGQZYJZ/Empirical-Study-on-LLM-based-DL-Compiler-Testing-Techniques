
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.nn.functional.linear(x1) 
        v2  = v1 * 0.5
        v3  = (v1 ** 3) * 0.044715
        v4  = v3  +  v2
        v5  = v4 * 0.7978845608028654 
        v6  = torch.tanh(v5)   
        v7  = v6   +  1
        return v7 * x1


# Initializing the model
m  = Model()
# Input to the model
x1 = torch.randn(3, 320) 

# Outputs of the model
