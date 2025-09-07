
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.convt  = torch.nn.ConvTranspose2d(3, 8, kernel_size=5)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1  = self.convt(x1)
        mask  = (v1 > 0).type(torch.cuda.FloatTensor) # create a mask for the positive values in the output of the transposed convolution operation
        v2 = torch.nn.functional.leaky_relu(v1, negative_slope=self.negative_slope) # apply the leaky relu function to the output of the transposed convolution operation
        output  = v2 * mask  # multiply the result of the leaky relu function by the mask
        return output


# Initializing the model