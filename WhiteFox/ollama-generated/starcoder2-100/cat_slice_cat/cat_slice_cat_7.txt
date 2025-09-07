
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input_tensors):
        t0 = torch.cat(input_tensors)
        t1 = t0[:, 0:9223372036854775807] # Slice the concatenated tensor along dimension 1
        t2 = t1[:, 0:size] # Further slice the tensor along dimension 1
        t3 = torch.cat([t0, t2], dim=1) # Concatenate the original concatenated tensor and the sliced tensor along dimension 1
        return t3


# Initializing the model
m = Model()
 
# Inputs to the model
input_tensors  = [torch.randn(100), torch.randn(20, 5)] # Input tensors to be concatenated together
 
