
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x): 
        v0  = self.conv(x) # Apply pointwise convolution with kernel size 1 to the input tensor
        v1  = F.relu(v0)   # Apply ReLU activation function to the output of the convolution
        return v1

m  = Model()

# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)

