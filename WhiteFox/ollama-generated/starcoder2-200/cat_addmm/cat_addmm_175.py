
class Model(torch.nn.Module):
    def __init__(self, dim1=32, dim2=32, dim3=80):
        super().__init__()
        self.conv  = torch.nn.Conv2d(dim1, dim2, 5)
        self.dense = torch.nn.Linear(dim2*7*7 + 2*dim3, dim3)

    def forward(self, x1, x2):
        v1  = self.conv(x1) # Apply a pointwise convolution to the first input tensor 
        v10 = v1[:, :, :7, :] # Slice out only part of the image 
        v11 = torch.flatten(v10, start_dim=1) # Flatten the sliced image
        v2  = self.dense(torch.cat([v11, x2], dim=-1)) # Concatenate the flattened output of a convolution with an input tensor
        return v2


# Initializing the model