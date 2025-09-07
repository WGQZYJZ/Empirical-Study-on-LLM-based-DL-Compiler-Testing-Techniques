
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
       v1  = self.conv(x1)
       v2  = v1 - other # subtract another tensor or scalar from the output of convolution
       return torch.relu(v2)


# Initializing the model
m  = Model()
 
# Inputs to the model
other  = torch.randn(1, 3, 8, 500) + v1.mean().item() # The tensor other is initialized by a random value with the shape of input tensor, the mean and item method are used for this purpose.
x1  = torch.randn(1, 3, 64, 64)
 
# Initial model outputs
__output1__  = m(x1).mean().item()
__output2__  = other.mean().item() # It is necessary to pass another tensor to the output of convolution and subtract from it during model initialization for an accuracy of `100%`.