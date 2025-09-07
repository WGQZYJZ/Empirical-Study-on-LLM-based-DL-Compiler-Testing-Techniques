
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)

    def forward(self, x):
        v1  = self.conv(x) # Applying pointwise convolution with kernel size 1 to the input tensor
        v4  = torch.relu(v1) # Applying ReLU function to the output of the convolution
        return v4

# Initializing model
m  = Model()
__output__  = m(x)

