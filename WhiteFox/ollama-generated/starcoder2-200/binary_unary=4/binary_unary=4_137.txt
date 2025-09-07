
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, other): # Pass in a new keyword argument 'other'
        v1  = self.linear(x1) 
        v2 = v1 + other
        v3  = torch.relu(v2)

        return v3

# Initializing the model
m = Model()

