
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, size=9223372036854775807):
        v1 = torch.cat([x1, x2], dim=1)  # Concatenate input tensors along dimension 1
        v2 = v1[:, 0:size]  # Slice the concatenated tensor along dimension 1
        v3 = v2[:, 0:size]  # Further slice the tensor along dimension 1
        v4 = torch.cat([v1, v3], dim=1)  # Concatenate the original concatenated tensor and the sliced tensor along dimension 1
        return v4
 
 # Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(5, 8, size=9223372036854775807)
x2 = torch.randn(5, 8, size=9223372036854775807)
