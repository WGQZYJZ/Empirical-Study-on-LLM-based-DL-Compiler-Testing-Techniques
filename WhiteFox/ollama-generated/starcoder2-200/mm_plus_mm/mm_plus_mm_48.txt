
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.mm(x1[0], x1[1]) # Matrix multiplication between input1 and input2
        v3  = torch.mm(x1[2], x1[3]) # Matrix multiplication between input3 and input4
        v5  = v1 + v3                # Addition of the results of the two matrix multiplications
        return v5

# Initializing the model
m = Model()

