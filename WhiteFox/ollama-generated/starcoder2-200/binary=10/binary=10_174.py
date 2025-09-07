
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1): 
        v2 = torch.nn.functional.linear(x1)
        return v2  + other
 
 
 # Initializing the model 
 m = Model()
 # Inputs to the model   
 x1  = torch.randn(10, 3, 64, 64)
 __output__=m(x1)

