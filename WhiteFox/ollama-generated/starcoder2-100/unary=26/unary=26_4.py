
class Model(torch.nn.Module):
    def __init__(self, nchannels=8, negative_slope = 0.5) :
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, nchannels, 1, stride=1, padding=1)
        self.negative_slope = negative_slope
    def forward(self, x):
        v1 = self.conv_transpose(x)
        v2 = (v1 > 0).float()
        v3 = v1 * (-self.negative_slope)
        v4 = torch.where(v2 == True , v1, v3 )
        return v4

# Initializing the model
m = Model()

 # Inputs to the model
x  = torch.randn(50, 8, 64, 64).cuda()

 # Generating the input tensor for the PyTorch model
input_tensor = np.random.randn(32, 128, 192)
input_tensor = np.array([input_tensor])
input_tensor = torch.from_numpy(input_tensor).float().cuda()

 # Generating the output tensor for the PyTorch model (output of the pointwise transposed convolution and Leaky ReLU operation)
__output__  = m(x, input_tensor)

