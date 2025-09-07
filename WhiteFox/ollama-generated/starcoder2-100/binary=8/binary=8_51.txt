

class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + other # Add another tensor to the output of the convolution
        return v2

# Initializing the model with 2 different tensors as "other" argument
m1 = Model(other=torch.randn(3,8,4))
m2 = Model(other=torch.randn(7,5,6))

 # Inputs to both models
x1_m1  = torch.randn(1, 3, 64, 64)
x1_m2 = x1_m1 + other # Add the input tensors of both models
__output__  = m1(x1_m1), m2(x1_m2)

