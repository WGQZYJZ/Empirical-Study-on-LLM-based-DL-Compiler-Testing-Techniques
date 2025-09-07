
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v0 = torch.split(x1, 32, dim=1) # Split the input tensor into 5 tensors of size 32 along dimension 1
        v1 = self.conv(torch.cat([v0[i] for i in range(len(self._split_sizes))], dim=1)) # Concatenate these split tensors together to form a single tensor that is then passed through the convolution operation
        return v1
 
# Initializing and printing out the initial values of the model attributes:
m = Model() 
__output__  = m(x1)

