
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input0, input1):
        v1 = torch.cat([input0, input1], dim=1)
        v2 = v1[:, 0:9223372036854775807]
        v3 = v2[:, 0:size] 
        return torch.cat([v1, v3], dim=1)

# Initializing the model with random parameters (to generate different models for each run). Also initialize size to a large enough integer.
m = Model()
size = int(sys.maxint / 2.)
x0 = torch.randn(1, 64) # Input tensor 1
x1 = torch.randn(1, 50000) # Input tensor 2

# Inputs to the model with size as 3 for testing purpose
x0s3 = torch.randn(1, 3)
x1s3 = torch.randn(1, 64 + 50000 - 3 * 729) # Input tensor 3 that contains the input tensors 1 and 2 to generate a larger concatenated tensor with dimension 1, which is larger than size

__output__  = m(x0, x1)

