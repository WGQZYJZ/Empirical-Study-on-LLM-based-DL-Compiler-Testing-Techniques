
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2 = torch.nn.functional.conv3d(x1)  # Apply 3D convolution on the input tensor
        v1 = torch.nn.functional.batch_norm(v2, ) 
        return v1

# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(4, 6, 8)
