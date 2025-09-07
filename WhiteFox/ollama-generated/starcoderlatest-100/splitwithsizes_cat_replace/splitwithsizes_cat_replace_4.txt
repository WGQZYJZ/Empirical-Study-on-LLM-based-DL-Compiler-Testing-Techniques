
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.split(x1, 200, dim=1) 
        v2 = [torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim=1) for split_tensor in v1] # Concatenate all the split tensors along the same dimension
        return torch.stack(v2)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
