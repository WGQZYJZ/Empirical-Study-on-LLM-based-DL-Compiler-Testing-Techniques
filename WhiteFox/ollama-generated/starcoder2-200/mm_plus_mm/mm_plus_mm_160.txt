
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1,stride=1)
 
    def forward(self, x1,x2,x3,x4):
      t1  = torch.mm(x1, x2) # Matrix multiplication between input1 and input2
      t2  = torch.mm(x3, x4) # Matrix multiplication between input3 and input4
      t3  = t1 + t2 # Addition of the results of the two matrix multiplications
      return t3

# Initializing the model
m = Model()

 # Inputs to the model