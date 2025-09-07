
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.matmul(x1, torch.transpose(x2, -2, -1)) / inv_scale 
        v3  =  v1.softmax(-1) # Compute attention weights using softmax
        v4  = v3 .matmul(v2)  # Take a weighted average of the value tensor
        return v4

# Initializing model and assigning values to inputs x1, x2, inv_scale
m  = Model()
inv_scale = 0.7071067811865476
x1  = torch.randn(100)
x2  = torch.randn(100)

