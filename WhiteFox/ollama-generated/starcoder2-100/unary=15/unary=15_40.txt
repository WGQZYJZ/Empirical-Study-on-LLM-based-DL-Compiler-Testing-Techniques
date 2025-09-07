
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v0 = torch.zeros_like(x1[:, :3], dtype=torch.float32) # Creating the 3rd channel with zeros
        v1 = self.conv(v0) # Applying a pointwise convolution to the zero channel
        v2 = F.relu(v1)   # Applying the ReLU activation function to the output of the convolution operation on the 3rd channel
        return v2


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(1, 4, 64, 64) # A random input tensor with four channels
__output__   = m(x1)            # Running the forward pass of the model on the input tensor
 