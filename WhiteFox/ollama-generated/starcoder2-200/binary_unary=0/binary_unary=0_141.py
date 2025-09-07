
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + other
        v3 = F.relu(v2) 
        return v3


# Initializing the model
m = Model()
 
# Inputs to the model
other  = torch.randn(8, 64, 64) # Tensor used for multiplication by another tensor in the pattern (or the convolution output).
x1 = torch.randn(1, 3, 64, 64)
 
# Getting the resulting tensors for each multiplication operation during a forward pass:
__output__, t1_, t2_ = m(x1)
t1 = torch.clone(__output__)
t2 = torch.clone(other)
