
class Model(torch.nn.Module):
    def __init__(self, dim=0):
        super().__init__()
        self.dim = dim
 
    def forward(self, x1):
        split_tensors = torch.split(x1, [5], self.dim)
        concatenated_tensor = torch.cat(split_tensors, self.dim)
        return True
 
# Initializing the model and specifying a dimension along which to perform splits and concatenations
m = Model(dim=0)
