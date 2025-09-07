
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3, x4):
        v1  = torch.mm(x1, x2) 
        v2  = torch.mm(x3, x4)   
        v3  = v1 + v2       
        return v3


# Initializing the model
m = Model()
__inputs__ = [torch.randn(1, 6), 
              torch.randn(50, 18),
              torch.randn(7933, 45), 
              torch.randn(5, 2)]
 
# Run the model on the inputs and observe output
for i in __inputs__:
    print(__output__  = m(*i))
