
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(320 * 8, 1)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = torch.sigmoid(v1)
        v3  = v1 * v2 
        return v3


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(4, 320*8) # Input 1
x2 = torch.randn(5, 320*8) # Input 2
x3 = torch.randn(6, 320*8) # Input 3

## Please find all instances of the pattern "t1 * t2" and output all three inputs that produce outputs.

