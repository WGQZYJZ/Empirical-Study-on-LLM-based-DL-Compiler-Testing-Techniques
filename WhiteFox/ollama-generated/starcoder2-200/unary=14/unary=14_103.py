
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, 1)
        self.activation = torch.nn.ReLU()
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = self.activation(v1)
        v3 = v1 * v2
        return v3

# Initializing the model
m = Model()

 # Inputs to the model
x1  = torch.randn(4, 3, 60, 85)
