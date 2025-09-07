
import torch
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):  # Linear transformation followed by ReLU activation in PyTorch
        v1 = self.linear_transformation(x1) 
        v3 = F.relu(v2) # Non-linearity after linear transformation
        return v4


class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(8, 16, kernel_size=(3, 3), stride=2)
 
    def forward(self, x4): # Apply pointwise convolution with kernel size (3, 3) and stride of two to the input tensor
        return self.conv(x4)

m = Model()

