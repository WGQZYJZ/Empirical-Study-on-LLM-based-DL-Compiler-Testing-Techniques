
class Model(torch.nn.Module):
    def __init__(self, size):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.cat(x1, dim=1)
        v2  = v1[:,0:9223372036854775807] # Concatenate input tensors along dimension 1
        v3 = v2[:,0:size] # Slice the concatenated tensor along dimension 1
        v4 = torch.cat([v1, v3], dim=1) # Concatenate the original concatenated tensor and the sliced tensor along dimension 1
        return v4


# Initializing the model
m = Model(70)


# Inputs to the model
x1  = [torch.randn(1, 64, 32), torch.randn(1, 9223372036854775807-70)] # The input tensors to be concatenated and sliced

