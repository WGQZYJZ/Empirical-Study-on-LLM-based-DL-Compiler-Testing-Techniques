
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.lin  = torch.nn.Linear(256 * 8, 10)
 
    def forward(self, x1): 
        v1  = self.lin(x1).view(-1, 8 ,10 ) 
        return torch.relu(v1)

# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(256 * 4) 
 