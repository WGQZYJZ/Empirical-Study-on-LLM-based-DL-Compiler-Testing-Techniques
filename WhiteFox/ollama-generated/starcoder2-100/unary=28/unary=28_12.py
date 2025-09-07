
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1): 
        v = self.conv(x2)  # Apply a linear transformation to the input tensor
        return v
 
 # Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(3, 50)

# Validity check for different inputs:
print(m(x1).shape == m(x2).shape)


