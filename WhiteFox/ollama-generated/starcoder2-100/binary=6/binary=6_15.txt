
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, weight=0) - 53
        return v1


# Initializing the model
m  = Model()

 # Inputs to the model (should be different from previous model input)
x2 = torch.randn(84793, 64)
 
 
 __output__  = m(x2)
