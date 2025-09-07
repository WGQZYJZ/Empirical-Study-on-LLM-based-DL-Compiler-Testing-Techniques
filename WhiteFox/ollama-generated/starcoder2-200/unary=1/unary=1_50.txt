
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64, 128)
 
    def forward(self, x1):
        v1  = self.linear(x1) #Applying linear transformation to the input tensor
        v2 = v1 * 0.5 
        v3 = v1 + (v1*v1*v1)*0.044715
        v4 = v3*0.7978845608028654 # Multiply the output of the linear transformation by 0.7978845608028654 
        v5 = torch.tanh(v4) # Applying hyperbolic tangent function to the output of the linear transformation
        v6 = v5 +1 
        v7 = v2*v6 
        return v7

# Initializing the model
m  = Model()

