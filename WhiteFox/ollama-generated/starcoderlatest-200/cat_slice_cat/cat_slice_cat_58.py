
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        t1 = torch.cat([x1, x1], dim=1) # Concatenate input tensors along dimension 1
        t2 = t1[:, 0:9223372036854775807] # Slice the concatenated tensor along dimension 1
        t3 = t2[:, 0:size] # Further slice the tensor along dimension 1
        t4 = torch.cat([t1, t3], dim=1) # Concatenate the original concatenated tensor and the sliced tensor along dimension 1
        return t4


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(50000, 64, 64)
