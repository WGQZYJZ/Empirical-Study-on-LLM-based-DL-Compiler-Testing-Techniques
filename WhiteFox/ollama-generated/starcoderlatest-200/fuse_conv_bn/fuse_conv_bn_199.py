
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, bn=False):
        conv = torch.nn.Conv2d(...)
        if bn:
            output = conv(x1)
        else:
            output = conv.forward(x1) # Fuse the convolution and batch normalization layers if `bn` is False
        return output

# Initializing the model
m = Model()


# Inputs to the model
input_tensor  = torch.randn(1, 3, 4, 6, requires_grad=True)
__output__  = m(input_tensor, bn=False) # `bn` is False, so we will not fuse the batch normalization layer and convolution layers
# input_tensor  = torch.randn(1, 2, 4, 6)
# __output__  = m(input_tensor) # Fuse the batch normalization layer with the functional API pattern


