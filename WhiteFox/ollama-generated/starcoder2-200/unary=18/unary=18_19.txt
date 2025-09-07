
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1): 
        v1 = self.conv(x2)   
        v3 = torch.sigmoid(v4)  # Apply the sigmoid function to the output of the convolution
        return v5


# Initializing the model
m  = Model()

# Inputs to the model
x2 = torch.randn(1, 8, 64, 64)
