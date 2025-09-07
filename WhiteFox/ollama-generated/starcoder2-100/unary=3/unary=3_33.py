import torch
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 * -5
        v3  = v1 + 4
        v4  = torch.relu(v3)
        v5  = v2 + v4
        return v5
m  = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
__output__= m(x1)
t1  =  torch.relu(-5  + 4) # Apply the ReLU function to (-5 + 4), the output is -1,  and return 0.0 if it's less than or equal to zero; return value otherwise  
t2  = t1  * conv(input_tensor)  # Apply pointwise convolution with kernel size 1 to the input tensor and multiply by the output of ReLU function (-5 + 4)
