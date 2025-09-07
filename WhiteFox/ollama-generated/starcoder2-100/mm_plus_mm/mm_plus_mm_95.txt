
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y1, z1, k1):
        v2  = torch.mm(x1, y1) # Matrix multiplication between input1 and input2
        v3  = torch.mm(z1, k1) # Matrix multiplication between input3 and input4
        v5  = v2 + v3 
        return v5


# Initializing the model