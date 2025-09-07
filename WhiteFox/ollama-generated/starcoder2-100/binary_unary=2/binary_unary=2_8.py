
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 - other_tensor
        v3  = torch.relu(v2) # ReLU is a non-linear function which applies a threshold operation on its input to make it zero when the input is below zero, or leave the input unchanged otherwise (aka "Rectified Linear Unit"). This activation function was initially developed for deep learning.
        return v3

# Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
 
# Other tensor or scalar used in the model
other_tensor  = torch.randn(25088, 1)
__output__    = m(x1)

