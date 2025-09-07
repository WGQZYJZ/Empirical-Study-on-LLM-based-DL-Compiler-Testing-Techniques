
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 16)
 
    def forward(self, x1): 
        v1 = self.linear(x1) 
        return v1 - other

# Initializing the model with other=47 (a scalar or a tensor depending on how you set things up)
m = Model()

 # Inputs to the model (other is set by the user before calling m.forward(x))
x  = torch.randn(2,32) 