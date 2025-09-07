
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.split(x1, 2, dim=0) # Split input tensor along dimension dim into three tensors of length split_sizes[0], split_sizes[1] and split_sizes[2]
        v2 = torch.cat([v1[i] for i in range(3)], dim=0) # Concatenate all the split tensors along dimension 0
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
