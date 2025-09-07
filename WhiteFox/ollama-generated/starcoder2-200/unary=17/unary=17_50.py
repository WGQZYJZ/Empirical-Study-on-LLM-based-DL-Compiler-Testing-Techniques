
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.convT(x1)
        v2 = F.relu(v1) # Apply the ReLU activation function to the output of the transposed convolution (use API torch.nn.functional.relu)
        return v2

# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
