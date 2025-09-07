
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convTrans  = torch.nn.ConvTranspose2d(3, 8, 1)

    def forward(self, x):
        v1  = self.convTrans(x)
        return relu_op(v1)

# Initializing the model
m  = Model()


# Inputs to the model
x  = torch.randn(1, 3, 64, 64) # This is a randomly generated input tensor with the shape (number of batch size=1), (number of channels), and (height/width dimensions). The number of channels in this case are 8, which matches that specified by the user.  The image heights and widths in this case should match those specified by the user for the number of input channels.
