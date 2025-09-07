
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = F.relu(v1) # Apply the ReLU activation function to the output of the convolution (without parentheses, since PyTorch requires a single argument in the Relu function)
        return v2


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(32, 3, 64, 64)
__output__  = m(x1)


