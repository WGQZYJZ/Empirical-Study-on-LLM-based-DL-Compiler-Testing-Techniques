
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(4,1)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 > 0 
        v3  = v1 * negative_slope  
        v4  = torch.where(v2, v1, v3) # where(v2, v1, v3) is implemented as follows: for each element in the boolean tensor v2, if the element is True choose the corresponding element from v1 and otherwise choose the corresponding element from v3
        return v4

# Initializing model
m  = Model()

 # Inputs to the model
x1  = torch.randn(8, 4)
__output__  = m(x1)