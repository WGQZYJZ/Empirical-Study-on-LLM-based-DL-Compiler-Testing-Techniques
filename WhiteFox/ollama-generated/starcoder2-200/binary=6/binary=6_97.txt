
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1)
        self.linear = torch.nn.Linear(3 * 64 * 64, 907)
 
    def forward(self, x):
        v1 = self.conv1(x) # Apply pointwise convolution with kernel size 1 to the input tensor
        v2 = v1 - other # Subtract 'other' from the output of the linear transformation
        
        return v2


# Initializing the model
m  = Model()
other  = torch.randn(3 * 64 * 64)

