
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(50, 10)
 
    def forward(self, x2):
        v7  = self.linear(x2) 
        v8 = v7 * 0.5 # Multiply the output of the linear transformation by 0.5
        v9 = v7 + (v7*v7*v7)*0.044715 # Add the output of the linear transformation to the output of the linear transformation cubed multiplied by 0.044715 
        v10= v9 * 0.7978845608028654 # Multiply the output of the previous operation by 0.7978845608028654
        v11 = torch.tanh(v10) # Apply the hyperbolic tangent function to the output of the previous operation 
        v12= v11 + 1 # Add 1 to the output of the hyperbolic tangent function  
        v13= v8 * v12 # Multiply the output of the linear transformation by the output of the hyperbolic tangent function
        return v13

# Initializing the model
m = Model()

# Inputs to the model
x2  = torch.randn(1,50) 
