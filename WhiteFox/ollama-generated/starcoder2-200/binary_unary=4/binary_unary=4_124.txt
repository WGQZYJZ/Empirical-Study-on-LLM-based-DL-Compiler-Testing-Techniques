
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64, 1)
 
    def forward(self, x1, **kwargs): # Note the usage of **kwargs
        v1 = self.linear(x1) 
        v2 = v1 + kwargs['other']    
        return F.relu(v2), v1

# Initializing the model
m = Model()

# Inputs to the model 
x1 = torch.randn(5, 64) # Input tensor for the linear transformation

