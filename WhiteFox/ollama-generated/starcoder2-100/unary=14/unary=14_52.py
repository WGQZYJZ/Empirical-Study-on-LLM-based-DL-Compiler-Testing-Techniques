
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.ConvTranspose2d(3, 8, 4)
        self.conv2 = torch.nn.Conv2d(8, 3, 7)
 
    def forward(self, x1):
        v1  = self.conv1(x1) # Applying pointwise transposed convolution on the input tensor
        v2  = v1 * tanh(v1) # Applying sigmoid function to the output of the transposed convolution and then multiply with the output of the transposed convolution
        v3  = self.conv2(v2) # Applying pointwise convolution with kernel size 7 on the output of the sigmoid function multiplication, resulting in the final output
        return v3

# Initializing the model
m  = Model()
 
# Input to the model
x1  = torch.randn(1, 3, 64, 64)
 
__output__  = m(x1)

