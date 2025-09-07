
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        l1 = self.conv(x1)
        l2  = l1 * torch.clamp(min=0, max=6, l1 + 3) # Multiply the output of the convolution by clamped output of linear transformation added with 3
        l3  = l2 / 8 # Divide the output of the multiplication by 8
        return v4


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

