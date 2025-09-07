
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + torch.randn(*v1.shape)  # You can substitute a random tensor with the shape of the output of conv() here for simplicity
        v3  = torch.relu(v2)
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(4, 8, 60, 65)
__output__  = m(x1)