
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + other # ADDER: The "other" tensor is passed as a keyword argument to the addition operation.
        return v2


# Initializing the model
m  = Model()
other = torch.randn(5, 3, 64, 64) # Tensor that will be added to the output of conv(x1). The shape is [5, 3, 64, 64]


# Inputs to the model
x1  = torch.randn(2, 3, 64, 64) # Input tensor for conv(x1)
__output__   = m(x1)
