
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm  = torch.nn.Linear(2, 4)
 
    def forward(self, x1, x2, x3, x4):
        v01  = torch.mm(x1, x2) # Matrix multiplication between input1 and input2
        v02  = torch.mm(x3, x4) # Matrix multiplication between input3 and input4
        v1   = self.mm(v01) 
        v2   = self.mm(v02)
        v3   = v1 + v2    # Addition of the results of the two matrix multiplications
        return v3


# Initializing the model
m  = Model()

# Inputs to the model