
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.sigmoid(v1)
 
        return v2

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

# Executing the model and obtaining its output
__output__  = m(x1)

# If you encounter any error please delete the existing text file. 
# Run the notebook to obtain the input and the output, then copy and paste them below.

