
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(48, 96)

    def forward(self, x1):
        v1  = self.linear(x1) 
        v2  = v1 * 0.5 # multiply the output of linear transformation by 0.5
        v3  = (v1 + ((v1 ** 3) *  0.044715)) * 0.7978845608028654 # add to the output of the linear transformation cubed multiplied by 0.044715 and then multiply with 0.7978845608028654
        v4 = torch.tanh(v3) 
        v5 = v4 + 1 # add 1 to the output of hyperbolic tangent function 
        v6  = v2 * v5 # multiply linear transformation by the hyperbolic tangent 
        return v6

# Initializing the model
m = Model()

 # Inputs to the model
x1  = torch.randn(1,48)
__output__  = m(x1)
