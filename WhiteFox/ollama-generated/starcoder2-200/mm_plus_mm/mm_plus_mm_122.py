
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm1 = torch.nn.functional.linear  # mm1: Matrix multiplication
        self.mm2 = torch.nn.functional.linear  # mm2: Matrix multiplication
 
    def forward(self, x1, x2, x3, x4):
         # t1 = self.mm1(x1, x2)
        v1 = self.mm1(x1, x2)  
        # t2 = self.mm2(x3, x4)
        v2 = self.mm2(x3, x4)
        # t3 = v1 + v2
        v3 = v1 + v2
        return v3


# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.randn(50, 60)
x2  = torch.randn(40, 80)
x3  = torch.randn(70, 90)
x4  = torch.randn(30, 100)
 
# Output of the model is returned from a call to the model
__output__  = m(x1, x2, x3, x4)