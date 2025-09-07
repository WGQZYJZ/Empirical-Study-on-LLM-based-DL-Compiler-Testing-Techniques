
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 8)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2 = v1 - other_input
        return v2


# Initializing the model
m = Model()
 
other_input  = torch.randn(4096, 32) # Random tensor that is used to generate 'other' in this example
 
 # Inputs to the model
x1  = torch.randn(85, 32)
 
 