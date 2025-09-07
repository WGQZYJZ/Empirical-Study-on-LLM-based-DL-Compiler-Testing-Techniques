
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = nn.functional.relu(v1) # Relu function is an alias for ReLU. In pytorch, there are two ReLU activation functions: one is torch.nn.ReLU(), and another is torch.nn.functional.ReLU(). It is recommended to use the function provided by the nn package.
        return v2


# Initializing model
m = Model()

# Input tensor for the model
x1  = torch.randn(1,3,64,64)

#