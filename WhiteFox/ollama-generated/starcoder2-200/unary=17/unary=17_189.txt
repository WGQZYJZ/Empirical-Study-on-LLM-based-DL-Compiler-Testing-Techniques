
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1)

    def forward(self, x1):
        v0 = F.relu(x1) # Apply the ReLU activation function to the input tensor
        v1  = self.conv(v0) 
        return v1


# Initializing the model
m  = Model()
__output__= m(torch.randn(2,8,36,36))