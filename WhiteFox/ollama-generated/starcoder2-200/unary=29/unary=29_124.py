
class Model(torch.nn.Module):
    def __init__(self, minv=0., maxv=128.):
        super().__init__()
        self.convtrans = torch.nn.ConvTranspose2d(3, 96, kernel_size=(5, 5), stride=(2, 2))
        self.maxval = torch.tensor([float(maxv)], dtype=torch.double)
 
    def forward(self, x): 
        v1  = self.convtrans(x) # Apply a pointwise transposed convolution to the input tensor
        v2 = torch.clamp_min(v1, self.maxval) # Clamp the output of the previous operation
        v3 = torch.clamp_max(v2, self.maxval*4.) # Clamp the output of the previous operation to a maximum value 
        return v3


# Initializing and running model
model  = Model()
outputs= model(inputs)
