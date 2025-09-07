
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(4,8)

    def forward(self, x1):
        v0  = x1[:,:2] # Sub-selecting the first two channels from each input tensor and concatenating them horizontally. Note that it is a PyTorch convention to concatenate horizontally (by putting the tensors together without modifying their dimensions).
        v1  = self.linear1(v0) # Apply a linear transformation to one of the sub-tensors, resulting in the output of size [batch_size x n_channels] 
        v2  = v1 + other  # Add another tensor (specified by keyword argument "other") to the output of the linear transformation
        return v2

# Initializing the model
m = Model()

