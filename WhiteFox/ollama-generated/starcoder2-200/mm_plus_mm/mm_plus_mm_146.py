
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y1, z1, q1):
        v1 = torch.mm(x1, y1) # Matrix multiplication between input1 and input2 
        v2 = torch.mm(z1, q1)  # Matrix multiplication between input3 and input4 
        v3 = v1 + v2          # Addition of the results of the two matrix multiplications
        return v3


# Initializing the model