
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y1, z1): 
        v1 = torch.mm(x1, y1)
        v2 = torch.mm(y1, z1)
        v3  = v1 + v2 # Addition of the results of two matrix multiplications
        return v3

# Initializing model
m = Model()

# Inputs to the model
x1  = torch.randn(4,5).to("cuda")
y1  = torch.randn(5,6).to("cuda")
z1  = torch.randn(789320,3)
