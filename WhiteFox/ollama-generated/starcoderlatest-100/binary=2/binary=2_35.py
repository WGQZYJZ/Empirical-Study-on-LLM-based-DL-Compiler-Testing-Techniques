
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 - other
        return v2
# Inputs to the model (the 0th and 2nd dimensions are different for each sample in 'x')
x1 = torch.randn(3, 3, 64, 64) # (batch size x number of channels x height x width)
x2 = torch.randn(4, 3, 64, 64) # (batch size x number of channels x height x width)
other1 = torch.randn(4, 8, 1, 1) # (other tensor shape for batch_size=3 and 4 respectively)
other2 = 0.75
__output__1 = m(x1, other1) # The input 'other1' should be the output of a convolution layer applied to the batch samples in 'x1'
__output__2 = m(x2, other2) # The input 'other2' is an ordinary constant


