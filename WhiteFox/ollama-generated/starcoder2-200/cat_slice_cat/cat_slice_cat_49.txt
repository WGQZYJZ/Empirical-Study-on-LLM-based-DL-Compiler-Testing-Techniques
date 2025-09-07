
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, *inputs):
        v1 = torch.cat(inputs, dim=1) # Concatenate input tensors along dimension 1
        v2 = v1[:, 0:9223372036854775807] # Slice the concatenated tensor along dimension 1
        v3 = v2[:, 0:size] # Further slice the tensor along dimension 1
        v4 = torch.cat([v1, v3], dim=1) # Concatenate the original concatenated tensor and the sliced tensor along dimension 1
        return v4
 
# Initializing the model with two tensors
m = Model()
x0 = torch.randn(2, 64, 75, 78)
x1 = torch.randn(3, 90, 102, 102)
__output__  = m(*inputs=[x0, x1])

