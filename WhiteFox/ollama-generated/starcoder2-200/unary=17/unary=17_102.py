
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convt = torch.nn.ConvTranspose2d(3, 8, 1, stride=1)
 
    def forward(self, x1):
        v1 = self.convt(x1)
        v2 = F.relu(v1) # Apply ReLU activation function to the output of the transposed convolution
        return v2
# Initializing the model