class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convt = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.convt(x1) 
        v2 = torch.sigmoid(v1) # Apply the sigmoid function to the output of the transposed convolution
        v3 = v1 * v2  # Multiply the output of the transposed convolution by the output of the sigmoid function
        return v3
