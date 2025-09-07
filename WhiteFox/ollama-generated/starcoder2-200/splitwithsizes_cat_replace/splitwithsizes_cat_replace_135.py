
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        split_tensors  = torch.split(x1, 256) 
        concatenated_tensor  = torch.cat([split_tensors[i] for i in range(len(split_tensors))], 3) 
        return concatenated_tensor

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 6072)

 # Initializing the model
m = Model()

# Inputs to the model
x1 = torch.rand((3, 8))

