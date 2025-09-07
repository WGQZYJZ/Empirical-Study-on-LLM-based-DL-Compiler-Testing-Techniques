
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.m1 = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = torch.mm(x1, x1) # Matrix multiplication between input1 and input2
        v2 = torch.mm(x1, x1) # Matrix multiplication between input3 and input4
        return v1 + v2

# Initializing the model
m = Model()


