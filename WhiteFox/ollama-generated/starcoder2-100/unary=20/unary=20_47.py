
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1) 
        v2  = torch.sigmoid(v1) 
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3840, 65536).reshape(3840, 75, 1, 1) # input with size [3840, 65536]. This is a sample. Please generate your own input tensor that fits the requirement.
