
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(20, 3)
 
    def forward(self, v1):
        v2 = v1 + 4 
        return self.linear(v2)

# Initializing the model
m = Model()

 # Inputs to the model
v1  = torch.randn(1, 50)

 __output__  = m(v1)
 