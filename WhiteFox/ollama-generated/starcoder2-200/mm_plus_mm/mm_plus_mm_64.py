
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2): 
        v1 = torch.mm(x1, 0) # Matrix multiplication between input1 and zero
        v2 = torch.mm(x2, 0) # Matrix multiplication between input3 and zero
        v3  = v1 + v2 # Addition of the results of two matrix multiplications
        return v3


# Initializing the model