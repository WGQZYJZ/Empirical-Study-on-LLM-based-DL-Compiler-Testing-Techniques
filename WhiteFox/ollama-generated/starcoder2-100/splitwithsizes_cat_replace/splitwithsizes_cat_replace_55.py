
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2  = torch.split(x1, [3,4], dim=0) 
        v5  = torch.cat([v2[i] for i in range(len(v2))], dim=0) 
        return v5

 # Initializing the model
 m = Model()
 
# Inputs to the model
 x1 = torch.randn(7, 64, 32)
 
 # Outputs from the model
 m(x1)
 
 # The output should be same as:
 
 v2  = torch.split(x1, [3,4], dim=0) 
 v5  = torch.cat([v2[i] for i in range(len(v2))], dim=0) 
 
v6 = torch.tensor([[v5[k][j] for k in range(7)] for j in range(32)])