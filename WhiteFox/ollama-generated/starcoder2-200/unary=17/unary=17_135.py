
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, 1)
        self.relu = torch.nn.ReLU()

    def forward(self, x):
        v1  = self.conv_transpose(x) 
        v2  = self.relu(v1)
        return v2


# Initializing the model
m = Model()
 
# Inputs to the model
x = torch.randn(4096, 3 ,64, 64) # Change this line according to your need. 
__output__  = m(x)

# Description of inputs