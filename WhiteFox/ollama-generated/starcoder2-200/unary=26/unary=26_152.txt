
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.2):
        super().__init__()
        self.convt  = torch.nn.ConvTranspose1d(3, 8, kernel_size=3, stride=4)
 
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1  = self.convt(x1)
        mask   = (v1 > 0).int()  # Convert to boolean tensor using torch.int() and then convert back to int8/uint8/float32/int64 as the input of where function
        v3  = v1 * negative_slope 
        return torch.where(mask, v1, v3)


# Initializing the model with negative slope parameter value -0.2