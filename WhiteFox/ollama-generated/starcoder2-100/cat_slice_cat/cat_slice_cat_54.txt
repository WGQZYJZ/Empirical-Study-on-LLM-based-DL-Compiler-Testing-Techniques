
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input_tensors):
        v1 = torch.cat(input_tensors, dim=1) 
        v2 = v1[:, 0:9223372036854775807] # Slice the concatenated tensor along dimension 1
        v3 = v2[:, 0:size]  # Further slice the tensor along dimension 1
        v4 = torch.cat([v1, v3], dim=1) 
        return v4


# Initializing the model with some input tensors 
tensors  = [torch.randn(35, 8923706, 10),
            torch.randn(35, 789648, 9)]
 
m = Model()
__output__  = m(tensors)

