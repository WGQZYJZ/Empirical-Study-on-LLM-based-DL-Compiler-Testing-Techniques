
class Model(torch.nn.Module):
    def __init__(self, num_units):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, num_units)
 
    def forward(self, x):
        v1 = self.linear1(x)
        v2  = torch.cat([v1], dim=1) # Concatenate the result along dimension 1
        return v2
# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1,3,64,64)
