
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.split_tensors = torch.nn.ModuleList()
 
    def forward(self, x1):
        v1  = torch.split(x1, [8], dim=1) # Split along the dimension with index `dim=1` (channel axis in PyTorch) and obtain a list of tensors
        concatenated_tensor = torch.cat(v1, dim=0) # Concatenate along the dimension with index `dim=0` (batch axis in PyTorch)
        return v4

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(32, 3, 64, 64)
