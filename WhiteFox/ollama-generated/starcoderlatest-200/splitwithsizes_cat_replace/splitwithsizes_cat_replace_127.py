
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.split_sizes = (64, 128) # Split along dimension of size 64 and 128
    
    def forward(self, x1):
        split_tensors = torch.split(x1, self.split_sizes, dim=0) 
        concatenated_tensor = torch.cat(split_tensors, dim=0)
        return concatenated_tensor


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 3, 64, 64)
