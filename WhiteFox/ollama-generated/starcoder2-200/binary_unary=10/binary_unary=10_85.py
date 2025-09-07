
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.linear = torch.nn.Linear(100, 5)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        
        v2  = other + v1
        v3  = nn.functional.relu(v2)
        return v3
 
# Initializing the model
m  = Model()


# Inputs to the model