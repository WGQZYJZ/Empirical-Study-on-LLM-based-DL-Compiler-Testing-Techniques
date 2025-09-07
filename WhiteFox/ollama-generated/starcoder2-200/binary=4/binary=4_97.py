
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.linear = torch.nn.Linear(in_features=7*7*64, out_features=10)
 
    def forward(self, x):
        v1 = self.conv(x) # Apply a pointwise convolution with kernel size 1 to the input tensor
        v2 = self.linear(v1) # Apply a linear transformation to the output of the pointwise convolution
        return v2

# Initializing model
m = Model()
 
# Inputs to the model
