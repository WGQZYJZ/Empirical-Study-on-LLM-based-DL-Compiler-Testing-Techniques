
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v4a_shape  = v1.shape
        v4b  = torch.randn(*v4a_shape) # A new random tensor of the same shape as the output of the convolution is created and assigned to another variable, for example "v4b"
        v2  = v1 + other # Another variable is added to the output of the convolution using a keyword argument named "other", and the addition operation adds another tensor. It is assumed that the tensor passed by "other" is the same as or more general than t4a_shape and that "v1" and "v2" have compatible shapes (for example, for 3x64x64 input and output tensors, the shape of a tensor created with torch.randn(torch.Size([8, 3, 7, 9])).shape would not be valid because the new tensor must have at least three dimensions.)
        return v2

# Initializing the model
m = Model()


