
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + 0.5 # adding 0.5 to the output of the convolution
        v3  = v1 * torch.tensor([[7], [4]])  # multiplying the output of the convolution by a 2D tensor
        v4  = v3[1] / v3[0] # dividing the output of the multiplication with index 1 in a 2D tensor to the value at index 0 in that same 2D tensor
        v5  = v1 + torch.tensor([9, 7])   # adding 9 and 7 to the output of the convolution 
        return v5 * v4


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)