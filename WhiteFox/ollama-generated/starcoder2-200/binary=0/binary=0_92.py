
class Model(torch.nn.Module):
    def __init__(self, conv_layer=torch.nn.Conv2d(3, 8, 1)):
        super().__init__()

        self.conv = conv_layer
        self._output_tensors = []
 
    def forward(self, x1):
        
        v1 = self.conv(x1)
        v2 = v1 + self._output_tensors[-1]
        return v2
        
# Initializing the model with torch.nn.Conv2d  # as argument
m  = Model()


# Inputs to the model:
x1  = torch.randn(1, 3, 64, 64)
m._output_tensors[-1] = x1  # Initialize _output_tensors attribute
__output__  = m(x1)  # Call forward method with inputs

