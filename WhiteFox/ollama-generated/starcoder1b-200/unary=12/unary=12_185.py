
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = F.sigmoid(self.conv(x1)) # Apply the sigmoid function to the output of the convolution
        v2 = v1 * torch.sin(x1) # Multiply the output of the convolution by the output of the sin function
        return v2


# Initializing the model
m = Model()


