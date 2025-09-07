
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1) # Pointwise convolution with kernel size 1
        v4  = (v1 + other)
        v5  = torch.relu(v4) 
        return v5


# Initializing the model
m = Model()
 
# Inputs to the model: 1st input, 2nd input and a tensor to add to the output of first input in the model
x1 = torch.randn(1, 3, 64, 64) # 1st input in the model for pointwise convolution with kernel size 1
other = torch.zeros([8], dtype=torch.float32).to(device='cuda') # A tensor to add to the output of first input in the model
 
__output__, __intermediate_outputs__ = m(x1)

