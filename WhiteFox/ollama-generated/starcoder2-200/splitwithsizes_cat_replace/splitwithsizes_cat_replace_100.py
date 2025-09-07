
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.split  = torch.nn.Split(dim=dim) 
        self.concat = torch.nn.Cat(dim=dim)
 
    def forward(self, x1):
        split_tensors  = self.split(x1) # 0.5, 3, 4, 2, 6, 8
        concatenated_tensor = self.concat([split_tensors[i] for i in range(len(split_sizes))]) # [0.5], [3, 4, 2, 6, 8]
        return concatenated_tensor


# Initializing the model