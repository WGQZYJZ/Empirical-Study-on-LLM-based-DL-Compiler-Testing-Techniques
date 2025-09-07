
class Model(torch.nn.Module):
    def __init__(self, other=0.5):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + other # Add another tensor to the output of the convolution
        return v2

# Initializing the model with 3 keyword arguments (a new input tensor is passed as an argument to the __init__ method; another input to the model is passed in the first call to the forward method)
m = Model(other=torch.randn((1,))) # Generate random 4D Tensor
__output__1 = m(x1)

