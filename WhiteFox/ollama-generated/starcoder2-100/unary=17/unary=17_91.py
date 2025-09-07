
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.deconv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.deconv(x1)
        v2  = F.relu(v1)

        return v2

# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(307,8,64,64) # Replace 8 with 307 and use a random number that is different from the previous one in your input tensor.
__output__  = m(x1)

