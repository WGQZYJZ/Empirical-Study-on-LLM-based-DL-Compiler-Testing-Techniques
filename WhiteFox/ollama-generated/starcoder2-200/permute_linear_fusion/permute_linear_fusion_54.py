
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v0 = torch.ones((2,), dtype=torch.long) # Dummy input for the first tensor creation to avoid "The 'permute' method does not exist." error 
        v1  = x1.permute(-3,-1).permute(-3,-2)[v0, :]
        v2  = torch.nn.functional.linear(v1, self.linear.weight)
        
        return v2
# Initializing the model
m = Model()

 # Inputs to the model (can be different from the previous example.) 
x1  = torch.randn(100,3,4,5)  

__output__  = m(x1)

