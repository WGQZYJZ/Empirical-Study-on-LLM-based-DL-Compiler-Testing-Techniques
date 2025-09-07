
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = sigmoid(v1)
        v3  = v1 * v2
        return v3


# Initializing the model
m  = Model()


 # Inputs to the model
__input_tensor__   = torch.randn(5, 8, 64, 64)

__output__  = m(__input_tensor__)

# Input tensor for a PyTorch GLU operation (in this example, the model takes three input channels with 64x64 input images): 5, 3, 64, 64

