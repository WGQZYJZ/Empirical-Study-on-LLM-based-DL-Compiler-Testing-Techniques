
class Model(torch.nn.Module):
    def __init__(self, input_size=1024):
        super().__init__()
 
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.linear = torch.nn.Linear(input_size + 8 * 64**2, input_size // 50, bias=False)
 
    def forward(self, x):
        v1 = self.conv(x) # Apply a convolution operation to the input tensor
        v2 = self.linear(v1) # Apply a linear operation on the output of the convolution with bias set to false
        return v2
 
# Initializing the model
m  = Model()
 
 
# Inputs to the model
input_tensor  = torch.randn(3, 8 * 64**2, 50) # Generate a random input tensor for the model
 
 