
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y2=0.5, z3='constant'):
        v4  = torch.erf(z3)  # Apply the error function to 'constant'
        
        return v4


# Initializing the model with 3 input values.
m = Model()
__output__, __output1__, __output2__ = m(x,y1=0.5, y2=0.7071067811865476)

