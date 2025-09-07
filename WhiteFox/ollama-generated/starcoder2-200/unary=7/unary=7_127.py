
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 40)
 
    def forward(self, x1):
         v1  = self.linear1(x1)
         v2 = torch.clamp(v1+3)
         v3 = v2 * v2
         v4 = torch.relu(v3)
         v5 = v2 / v4
         return v5

# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(6, 3)
 
 __output__  = m(x1)

 