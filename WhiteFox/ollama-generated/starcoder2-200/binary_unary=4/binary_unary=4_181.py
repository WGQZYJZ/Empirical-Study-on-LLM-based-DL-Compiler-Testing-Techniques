
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1): 
        v1  = self.linear1(x) 
        v2  = v1 + self.weight 
        v3  = torch.relu(v2) 
        return v3 

# Initializing the model 
m = Model()

# Inputs to the model 
other_tensor = torch.rand((4, )) 
x = torch.randn(5, 784) 
