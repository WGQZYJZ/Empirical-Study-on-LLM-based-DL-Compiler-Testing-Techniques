
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2, y3, z4):
        v0 = torch.mm(x1, x2) 
        v1  = torch.mm(y3, z4) # Matrix multiplication between input1 and input3
        v2  = v0 + v1  # Addition of the results of the two matrix multiplications
        return v2

# Initializing model
m  = Model()

