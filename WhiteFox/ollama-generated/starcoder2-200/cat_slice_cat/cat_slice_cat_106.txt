
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    
    def forward(self, input_tensors):
        v0 = torch.cat(input_tensors) # Concatenate tensors of dimension 3 along dimmension 1
        v1 = v0[:, :int(9223372036854775807)] # Slice the concatenated tensor along the dimension 1 
        v2 = v1[:v] # Slice the sliced tensor along the dimension 1 (this is to ensure the tensor has the desired size)
        v3 = torch.cat([v, v], dim=1) # Concatenate both tensors along dimension 1
        return v3


# Initializing the model
m = Model()

# Inputs for the model and its dimensions
input_tensors0  = [torch.randn(549836972, 3), torch.randn(23)]
input_tensors1  = [torch.randn(17, 3)]
 
__output__  = m(input_tensors)

