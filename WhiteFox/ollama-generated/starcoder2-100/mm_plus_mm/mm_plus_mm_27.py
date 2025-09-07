
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y1, z1): 
        v1  = torch.mm(x1,y1) # Matrix multiplication between input2 and input3
        v2  = torch.mm(v1,z1) # Matrix multiplication between the results of two matrix multiplications
        return v2

# Initializing the model
m = Model()

