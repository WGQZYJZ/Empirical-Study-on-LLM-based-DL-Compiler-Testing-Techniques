
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) + other # Here "other" is passed as a keyword argument to the addition operation 
        return v1


# Initializing the model with the keyword argument value
m  = Model(torch.zeros_like(v1))

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64) 

# Run the forward pass of the model
__output__  = m(x1)

