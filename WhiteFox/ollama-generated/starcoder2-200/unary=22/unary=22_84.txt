
class Model(torch.nn.Module):
    def __init__(self, num_classes=30):
        super().__init__()
        self.linear = torch.nn.Linear(64*64*3, 128)
 
    def forward(self, x1):
        v1  = self.linear(x1.view(-1)) # Apply a linear transformation to the input tensor and reshape it into a 1D vector 
        v2  = torch.tanh(v1)   # Apply the hyperbolic tangent function to the output of the linear transformation, which should be between -1 and +1
        return v2


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(3000, 64*64*3)
__output__  = m(x1)