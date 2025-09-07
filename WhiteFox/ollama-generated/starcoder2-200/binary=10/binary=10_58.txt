
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, other=None): # Add another tensor argument here (keyword argument)
        v = torch.nn.Linear()(x1)
        if other is not None:
            v  = v + other 
        return v

# Initializing the model with an argument
m  = Model()
v_expected  = m(torch.randn(2,5), other=None) # If other=None in the call to m(), you should expect the same output as before this code snippet
