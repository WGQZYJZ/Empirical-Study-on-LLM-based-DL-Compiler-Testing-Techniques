
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v3  = torch.matmul(x1, x2) / 0.7071067811865476
        v4  = torch.nn.functional.softmax(v3.div(-2), dim=-1) 
        v5  = v4 + 1
        return v5


# Initializing the model
m  = Model() 

# Inputs to the model
x1 = torch.randn(8, 8) # random query tensor of size (8 x 8)
x2 = torch.randn(8, 8) # random key/value tensor of size (8 x 8)

