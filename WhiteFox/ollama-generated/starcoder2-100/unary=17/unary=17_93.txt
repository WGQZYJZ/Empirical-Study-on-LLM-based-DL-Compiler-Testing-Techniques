
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
        self.relu = torch.nn.ReLU()
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.relu(v1)
        return v2


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64) # This is the input for the first example of the model. Notice that the size and the number of channels differ from the previous model.
__output__  = m(x1)

