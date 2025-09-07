
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.sigmoid(v1)
        return v2

# Initializing the model with an input tensor and its label in float format. It is required that the labels are real-valued and have the same shape as the input tensors.
m  = Model()
x1 = torch.randn(1,3,64,64)


# The output from the model without the forward pass.
__output__  = m(x1)


