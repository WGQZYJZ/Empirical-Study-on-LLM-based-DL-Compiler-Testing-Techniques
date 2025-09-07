
class Model(torch.nn.Module):
    def __init__(self, kernel_sizes=(2, 1)):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, kernel_sizes[0], stride=kernel_sizes[0])
 
    def forward(self, x1):
        v1 = self.conv(x1)
        if len(v1.shape) != 4:
            # raise ValueError('The input tensor should be a 4-D array.')
            raise NotImplementedError("The model for pointwise convolution doesn't support this shape.")
 
        v2 = torch.split(v1, kernel_sizes, dim=-1)[0]
        if len(v2.shape) != 4:
            # raise ValueError('The input tensor should be a 4-D array.')
            raise NotImplementedError("The model for pointwise convolution doesn't support this shape.")
 
        v3 = torch.cat([torch.split(x1, kernel_sizes)[i] * 0.5 for i in range(len(kernel_sizes))], dim=-1)
        if len(v3.shape) != 4:
            # raise ValueError('The input tensor should be a 4-D array.')
            raise NotImplementedError("The model for pointwise convolution doesn't support this shape.")
 
        v4 = torch.split(torch.erf(v3), kernel_sizes, dim=-1)[0]
        if len(v4.shape) != 4:
            # raise ValueError('The input tensor should be a 4-D array.')
            raise NotImplementedError("The model for pointwise convolution doesn't support this shape.")
 
        v5 = torch.cat([torch.split(v2, kernel_sizes)[i] * v4[i] for i in range(len(kernel_sizes))], dim=-1)
        if len(v5.shape) != 4:
            # raise ValueError('The input tensor should be a 4-D array.')
            raise NotImplementedError("The model for pointwise convolution doesn't support this shape.")
 
        v6 = torch.cat([x1 * v5[i] for i in range(len(kernel_sizes))], dim=-1)
        if len(v6.shape) != 4:
            # raise ValueError('The input tensor should be a 4-D array.')
            raise NotImplementedError("The model for pointwise convolution doesn't support this shape.")
 
        return v6


# Initializing the model
m = Model((2, 1))
