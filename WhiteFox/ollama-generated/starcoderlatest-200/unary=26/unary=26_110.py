
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, kernel_size=(3, 4), stride=(2, 2), padding=(1, 2))
        self.negative_slope = negative_slope
 
    def forward(self, x):
        v1 = self.conv_transpose(x)
        v2 = torch.where((v1 > 0), v1, (v1 * self.negative_slope))
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 3, 64, 64)
