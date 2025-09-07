
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1) # Apply the convolution on input tensor `v`
        v2  = torch.sigmoid(v1)  # Apply sigmoid activation function on output of the previous operation
        return v2


# Initializing model:
m  = Model()

# Input tensors to model m
x1  = torch.randn(4,3 ,56,56 )


# Expected Results:
__output__  = m(x1)


