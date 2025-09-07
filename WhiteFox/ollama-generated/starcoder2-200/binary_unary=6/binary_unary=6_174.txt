
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(32,10)
 
    def forward(self, x1):
       v1  = self.lin(x1)
       v2  = v1 - other # Replace 5 with the value of 'other' in the pattern above
       return relu(v2)

# Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.randn(3,32) # replace 3 by the number of input nodes from the previous model

