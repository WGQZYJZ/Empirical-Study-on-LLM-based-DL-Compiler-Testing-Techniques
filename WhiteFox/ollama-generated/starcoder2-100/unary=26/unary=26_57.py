
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.convt  = torch.nn.ConvTranspose2d(8, 3, kernel_size=(5, 5), padding=(4, 2)) # Apply pointwise transposed convolution to the input tensor
        self._relu  = torch.nn.LeakyReLU(negative_slope)
 
    def forward(self, x1):
        v1 = self.convt(x1)
        mask  = v1 > 0 
        v3 = self._relu(v1 * -0.7549062874999997)
        v4 = torch.where(mask, v1, v3) # Apply the where function to select elements from t1 or t3 based on the mask t2
        return v4

# Initializing the model
m  = Model()


# Inputs to the model