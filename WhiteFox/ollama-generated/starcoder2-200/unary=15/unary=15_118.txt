
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)

    def forward(self, x1):
        v1  = self.conv(x1) # Apply a pointwise convolution to the input tensor
        v2  = torch.nn.ReLU()(v1) # Apply ReLU activation function on the output of convolution
        return v2

# Initializing model with different weights and biases for the model
m_init  = Model()

