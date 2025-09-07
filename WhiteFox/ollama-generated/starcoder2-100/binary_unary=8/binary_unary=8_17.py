class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
       v1 = self.conv(x1)
       v2 = F.relu(v1 + torch.rand(*v1.shape) * 0.5)    # Added the ReLU activation on the result of the pointwise convolution + bias
       return v2
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
       v1 = F.leaky_relu(v1 + torch.rand(*v1.shape)) # Added the LeakyReLU activation on the result of the pointwise convolution
       return v1
    def same(input):
        result1 = model1.forward(input)
        result2 = model2.forward(input)
        
        # return True if they are both equal (for us it means that they will be equal) or False otherwise.
        return torch_funk.diff(result1, result2)
    output = input.size() * 30
   return (input > 1e-4) * input + (input < -1e-4) * slope * ((1e-4 - input).abs()**3)
