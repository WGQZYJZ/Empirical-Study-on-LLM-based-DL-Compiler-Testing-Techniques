
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(8, 3, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.tanh(v1)
        return v2


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(8, 3, 64, 64) # Change the shape of this tensor as desired, ensuring that it is compatible with the forward call in the model. The model should take an input tensor of shape (N x 8 x Hin x Win), where N = batch size, 8 = number of channels in the output tensor, and Hin x Win are the height and width of the output tensor, respectively
__output__  = m(x1)

