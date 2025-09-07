
class Model(torch.nn.Module):
    def __init__(self, split_sizes=5000):
        super().__init__()
        self.split  = torch.nn.Split(split_sizes)
        
    def forward(self, x1): 
        v2  = self.split(x1)[0] # split the input tensor into several tensors with length 5000
        v3  = torch.cat([v2 for i in range(len(split_sizes))], dim=0) # Concatenate the split tensors along dimension 0
        return v3


# Initializing the model