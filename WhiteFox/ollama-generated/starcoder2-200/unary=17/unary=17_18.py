
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.nn.functional.conv_transpose2d(x1, 8) 
        v3 = self.conv()
        return v3
 
    def conv(self):
       self.conv = nn.ConvTranspose2d(64*95*7+95*2*2*7, 8*7, kernel_size=2, stride=(1, 1), padding=(0, 0))
       return self.conv
# Initializing the model
m = Model()

 # Inputs to the model
 x1  = torch.randn(13456, 95)
 
