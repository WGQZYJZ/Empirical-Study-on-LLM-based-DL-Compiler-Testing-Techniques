
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        conv = torch.nn.Conv3d(in_channels=2, out_channels=2)
        bn  = torch.nn.BatchNorm3d(num_features=2)

        # Input  tensor for the Conv3d
        v1  = x1[:, :2, :, :] 
        v2 = conv(v1)
        
        v4 = bn(v2)
        return v4

# Initializing the model 
m = Model()


# Inputs to the model 
x1  = torch.rand(size=(30, 2, 5)) 

__output__= m(x1).shape # Output tensor shape should match 6, 2, 5
