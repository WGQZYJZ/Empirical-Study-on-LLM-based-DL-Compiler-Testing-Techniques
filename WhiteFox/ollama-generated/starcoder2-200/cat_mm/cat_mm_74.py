
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(20, 30)
 
    def forward(self, x1):
        v1  = self.linear(x1) 
        v2  = torch.mm(v1, t2) 
        return torch.cat([v2] * 4 + [v2]) 

# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(10, 30)
t2  = torch.randn(50, 20)
