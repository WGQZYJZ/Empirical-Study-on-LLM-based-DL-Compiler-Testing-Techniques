
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
         v1  = torch.einsum('ij...,jk...', [x1, x2])  # compute einsum of i-j...k
         v3  = v1 * (v2 + 0.) / math.sqrt(math.sqrt(v2.size(-1)))  # compute normalized dot product and divide by square root of value
         return v3

# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.rand(8, 4) + 0.5 
 x2  = torch.randn(64, 8, 4) + 0.5 
