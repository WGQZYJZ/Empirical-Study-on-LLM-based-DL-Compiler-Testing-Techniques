
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2 = self.linear_(x1)  # Linear transformation
        v3 = v2 - other        # Subtract 'other' from the output of the linear transformation
        return v3
 
# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(8, 6400)   
other  = 5.7e+9  # Tensor or scalar that is subtracted from the output of the linear transformation
 
 __output__  = m(x1)
 