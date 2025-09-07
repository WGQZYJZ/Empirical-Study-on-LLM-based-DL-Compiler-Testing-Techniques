
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        split = torch.split(x1, 5000, dim=3) 
        concatenated = torch.cat([split[i] for i in range(len(split))], dim=3)
        return concatenated


# Initializing the model
m = Model() 

# Inputs to the model
input_tensor  = torch.randn(2, 10000, 64, 78).long() # The shape of `input_tensor` is `(2, 10000, 64, 78)`. The total size along each dimension is 395,000. The total size in memory is therefore more than 1GB


