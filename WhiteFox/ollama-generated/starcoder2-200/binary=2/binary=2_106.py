
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 - other
        return v2


# Initializing the model
m = Model()

 # Inputs to the model
other  = torch.randn(1, 3, 64, 64) # Other is a random tensor with the same shape as x1 above
x1  = torch.randn(1, 3, 64, 64)  # x1 also is a random tensor

 # Initializing a new model with different inputs to verify that the first model works when feeding the second input and vice versa.

other_2  = torch.randn(1, 3, 58, 79) # Other is another random tensor with a different shape from other above

 x1  = torch.randn(4, 3, 64, 64) # x1 is also randomly initialized with a shape that is different from the input to the previous model and the shape of 'other'
 __output__  = m(x1)