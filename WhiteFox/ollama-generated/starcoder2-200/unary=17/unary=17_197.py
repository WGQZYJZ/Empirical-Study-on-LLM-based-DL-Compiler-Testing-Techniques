
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.convT(x1)
        v2 = torch.relu(v1) # Applying the ReLU activation function to the output of the transposed convolution
        return v2


# Initializing the model