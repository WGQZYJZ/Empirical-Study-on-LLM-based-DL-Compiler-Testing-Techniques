
class Model(torch.nn.Module):
    def __init__(self, size):
        super().__init__()
        self.size = size
 
    def forward(self, t):
        return torch.cat([t, t[:, :, :self.size]], dim=1)


# Initializing the model 
m = Model(6400)
 
# Input to the model is a tensor of shape [2, 3, 5] (randomly generated). 
# Output: A concatenated tensor with shape [2, 9223372036854775807, 6400], where 6400 is the size that was passed in.  
