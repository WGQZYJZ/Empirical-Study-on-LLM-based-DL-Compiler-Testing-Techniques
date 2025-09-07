
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input_tensors):
        # Input tensors: 3 tensors of shape [batch size = 2048 x 1] (for example)
        # Concatenate along dimension 1
        v1  = torch.cat(input_tensors, dim=1) 
        # Slice the concatenated tensor along dimension 1
        v2  = v1[:, 0:9223372036854775807] 
        # Further slice the tensor along dimension 1
        size = input_tensors[0].shape[-1] + input_tensors[1].shape[-1] 
        # Slice the concatenated tensor along dimension 1
        v3  = v2[:, 0:size] 
        # Concatenate the original concatenated tensor and the sliced tensor along dimension 1
        v4  = torch.cat([v1, v3], dim=1)
        return v4

# Initializing the model
m = Model()
 
# Inputs to the model (the number of tensors must match the length in the input_tensors argument for torch.nn.Module.forward)
input_tensors  = [torch.randn(2048, 1), 
                  torch.randn(2048, 3)]
__output__  = m(input_tensors)

