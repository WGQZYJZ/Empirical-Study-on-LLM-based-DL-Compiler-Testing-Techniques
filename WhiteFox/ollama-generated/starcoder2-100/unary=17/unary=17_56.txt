
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.deconv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.deconv(x1)
        v2 = F.relu(v1) # Applying ReLU activation function to the transposed convolution output.
        return v2

# Initializing model
m  = Model()
 
# Input tensors
x1= torch.randn(1,3,64,64)


