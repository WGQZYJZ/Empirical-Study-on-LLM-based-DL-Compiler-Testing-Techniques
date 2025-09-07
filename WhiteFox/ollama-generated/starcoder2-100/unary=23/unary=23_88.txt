
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convtranspose = torch.nn.ConvTranspose2d(3, 8, kernel_size=1)
 
    def forward(self, x):
        v1  = self.convtranspose(x) 
        return torch.tanh(v1)


# Initializing the model and passing an input to it as an example
m = Model()
input = torch.randn(1,3,64,64)
output = m(input)

# Output tensor shape: (batch size, number of channels, height of input data, width of input data)
expected_output  = (1,8,62,62)