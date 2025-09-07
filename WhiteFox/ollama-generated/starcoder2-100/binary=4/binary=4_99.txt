
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32,16)
 
    def forward(self, x1):
        v1  = self.conv(x1) + self.linear(v1) # Applying linear transformation to the output of a convolution layer
        return v1


# Initializing the model