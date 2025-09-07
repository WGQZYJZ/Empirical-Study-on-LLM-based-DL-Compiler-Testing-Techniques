
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, t1, t2):
        v1 = torch.cat([t1, t2], dim=1) # Concatenate input tensors along dimension 1
        v2 = v1[:, 0:9223372036854775807] # Slice the concatenated tensor along dimension 1
        v3 = v2[:, 0:size] # Further slice the tensor along dimension 1
        v4 = torch.cat([v1, v3], dim=1) # Concatenate the original concatenated tensor and the sliced tensor along dimension 1
        return v4


# Initializing the model
m = Model()

# Inputs to the model
t1 = torch.randn(2048, 1, 64, 64)
t2 = torch.randn(1953917, 1, 64, 64)
