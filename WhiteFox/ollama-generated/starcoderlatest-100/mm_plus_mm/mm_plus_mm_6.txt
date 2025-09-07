
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.m1 = torch.nn.Linear(16, 32)
 
    def forward(self, x1):
        t1 = torch.mm(x1, x1.transpose(-2, -1)) # Matrix multiplication between input1 and input2
        t2 = torch.mm(x1, x1.transpose(-2, -1)) # Matrix multiplication between input3 and input4
        t3 = t1 + t2 # Addition of the results of the two matrix multiplications
        v  = self.m1(t3)
        return v
 
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(64, 16, dtype=torch.float32)
