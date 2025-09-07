
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, y1, y2):
        t1  = torch.mm(x1, y1) # Matrix multiplication between input1 and input3
        t2  = torch.mm(y2, x2) # Matrix multiplication between input4 and input2
        t3  = t1 + t2 # Addition of the results of the two matrix multiplications

# Initializing the model
m  = Model()

