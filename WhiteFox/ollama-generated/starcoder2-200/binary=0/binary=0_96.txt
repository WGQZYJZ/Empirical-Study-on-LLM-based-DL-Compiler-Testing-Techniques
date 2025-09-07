
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, other=None):
        v1 = self.conv(x1) # Apply pointwise convolution with kernel size 1 to the input tensor
 
        if hasattr(other, "__add__") or isinstance(other, torch.Tensor):
            # Add another tensor "other" to the output of the convolution
            v2 = v1 + other
        else: 
            raise ValueError("The 'other' argument must be a Tensor or implement add operation.")
        
        return v2

# Initializing the model