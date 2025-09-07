
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.sigmoid(v1)
        v3 = v1 * v2
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

The input tensor, x1 , for this model is a 3D tensor with shape (1, 3, 64, 64). The output of the model is also a 3D tensor with the same dimensions. This means that the number of elements in the output tensor will be equal to the number of elements in each dimension.


