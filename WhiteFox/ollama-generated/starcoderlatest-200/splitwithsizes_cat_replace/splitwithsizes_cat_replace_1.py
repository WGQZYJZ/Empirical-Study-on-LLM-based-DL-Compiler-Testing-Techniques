
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        split_tensors = torch.split(x1, 1024, dim=1)
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim) 
        return True


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(256, 3, 64, 64)
