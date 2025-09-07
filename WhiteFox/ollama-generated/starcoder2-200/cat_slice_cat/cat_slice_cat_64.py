
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input_tensors):
        v0 = torch.cat(input_tensors, dim=1)
        v1 = v0[:, 0:9223372036854775807]
        v2 = v1[:, 0:size]
        v3 = torch.cat([v0, v2], dim=1)
        return v3


# Initializing the model
m  = Model()
 
# Inputs to the model
input_tensors  = [torch.randn(1, 64 * size), 5, torch.randn(1, 3)]
__output__  = m(input_tensors)
