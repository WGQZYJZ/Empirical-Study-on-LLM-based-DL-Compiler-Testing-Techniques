
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) * torch.randn_like(v1) # Add randomness to the output of the convolution
        v2 = (torch.erf(v1).relu() - 1) / 4 # Scale the output with ReLU function
        v3 = torch.sqrt(2 / math.pi) * torch.exp(0.5 * v2 ** 2) # Apply the Erf function to multiply with the inverse scale
        return v3


# Initializing the model
m = Model()


