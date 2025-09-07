
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1, stride=1)
 
    def forward(self, x1):
        v0 = torch.sigmoid(x1) # Add 1 to the output of the error function
        return v0


# Initializing the model
m  = Model()

 # Inputs to the model
x2  = m(torch.randn(3)) 

