
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.conv3d(x1) 
        return torch.nn.functional.batchnorm4d(v1)


# Initializing the model
m  = Model()

# Inputs to the model
input_tensor = torch.randn(2, 3, 5, 4, 6) # [N, C, D, H, W] tensor input for Conv3d
