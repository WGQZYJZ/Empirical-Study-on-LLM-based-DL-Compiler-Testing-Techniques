
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 3)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 * 0.5
        v3 = (v1*v1*v1)*0.44716 
        v4=v3*.79788
        v5 = torch.tanh(v4)+1 #Hyperbolic tangent is applied to the previous operation, and then `1` is added to the output of the hyperbolic tangent function
        v6  = v2 * v5
        return v6


# Initializing the model
m = Model()
 

# Inputs to the model
x1 = torch.randn(3,2)
