
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input_tensors: List[torch.Tensor]):
        v1 = torch.cat(input_tensors, dim=1) # Concatenate input tensors along dimension 1
        v2 = v1[:, 0:9223372036854775807] # Slice the concatenated tensor along dimension 1
        v3 = v2[:, 0:size] # Further slice the tensor along dimension 1
        v4 = torch.cat([v1, v3], dim=1) # Concatenate the original concatenated tensor and the sliced tensor along dimension 1
        return v4

# Initializing the model
m = Model()
 
# Inputs to the model - List of 5 tensors with different shapes
input_tensors = [torch.rand(3, 29),
                 torch.rand(700, 8, 63),
                 torch.rand(size[1], 14),
                 torch.rand(size[1], size[0], 15)]
 
__output__  = m(input_tensors)
