
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1): 
        v1  = self.conv(x1) # Pointwise convolution with kernel size 1 to the input tensor  
        v2  = v1 + torch.rand_like(v1)
        v3  = torch.relu(v2) # Apply ReLU activation function on the result of adding another random tensor to the output of the convolution
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 8, 64, 64)
