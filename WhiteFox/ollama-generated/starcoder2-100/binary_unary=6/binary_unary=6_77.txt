
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3,8)
 
    def forward(self, x2): 
        v1  = self.linear1(x2)  
        v2  = v1 - other
        v3  = torch.relu(v2)   
        return v3

# Initializing the model
m  = Model()
 
other  = [0., 0., 0.] # A vector of zeros
 
# Inputs to the model
x2  = torch.randn(1, 3, 8, 4)
__output__  = m(x2)

