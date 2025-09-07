
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 3)

    def forward(self, x):
        v1 = self.linear(x) 
        v2 = torch.tanh(v1) # Applying the hyperbolic tangent function to the output of the linear transformation.
        return v2

# Initializing model
m  = Model()
