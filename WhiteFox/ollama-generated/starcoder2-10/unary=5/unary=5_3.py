
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(8, 3, 1)

    def forward(self, x):
         v1  = F.interpolate(x, scale_factor=0.5) # Transposed convolution, with kernel size 1
         v2  = v1 * 0.5                             # Transposed convolution, with kernel size 1
         v3  = v1 * 0.7071067811865476               # Transposed convolution, with kernel size 1
         v4  = torch.erf(v3)                         # Error function
         v5  = v4 + 1                                # Add 1 to the output of the error function 
         v6  = v2 * v5                              # Output of the transposed convolution by another constant, which is the error function’s output 
         return v6
