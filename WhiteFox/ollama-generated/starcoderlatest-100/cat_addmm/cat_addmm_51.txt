
class Model(torch.nn.Module):
    def __init__(self, in_channel=32, out_channel=64, kernel_size=(1, 1), stride=(1, 1)):
        super().__init__()
 
        self.conv = torch.nn.Conv2d(in_channels=in_channel, out_channels=out_channel, kernel_size=kernel_size,
                                      stride=stride)
 
    def forward(self, x):
        mat1 = torch.rand((64, 32, 1, 1))
        mat2 = torch.rand((64, 64, 1, 1))
 
        t1 = torch.addmm(x, mat1, mat2) # Perform a matrix multiplication of mat1 and mat2 and add it to the input
        t2 = torch.cat([t1], dim=3)    # Concatenate the result along dimension 3 which is the fourth axis
 
        return t2


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 32, 64, 64)
