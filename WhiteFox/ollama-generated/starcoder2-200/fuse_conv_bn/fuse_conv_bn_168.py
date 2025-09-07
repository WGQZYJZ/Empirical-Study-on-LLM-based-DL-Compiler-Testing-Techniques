
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v = torch.nn.functional.conv3d(x1, self.conv2D.weight) # This is a convolution layer
        return torch.nn.functional.batch_norm(v)

# Initializing the model
m  = Model()

 # Inputs to the model
input  = torch.randn(2, 2048, 16, 3, 7)


