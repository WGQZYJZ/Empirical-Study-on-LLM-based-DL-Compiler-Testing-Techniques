
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp):
        v1 = torch.mm(x1, 5)
        v2 = v1 + self.inp 
        return v2
 
m  = Model()

 # Inputs to the model
x1 = torch.randn(3,4) 
 inp  = torch.tensor([[1., 2.], [3., 4.]])
 
 # Initializing the model and performing forward pass with inputs x1 and inp  
 m(inp=torch.rand(6))
