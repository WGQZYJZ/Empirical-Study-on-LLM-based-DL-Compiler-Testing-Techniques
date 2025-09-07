
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):  # Note: only one torch.split and one torch.cat operation is expected!
        v = [x1]
        for i in range(len(x1)):
            v[i] = v[i].unsqueeze(-1).unsqueeze(-1)
        v0  = self._splitwithsizes_cat(v, 32) # Custom torch operation
        return v0
    
    def _splitwithsizes_cat(self, tensors, split_size): # Note: only torch.split and one torch.cat is expected!
        splitted_tensors = []
        for i in range(len(tensors)):
            splitted_tensors += [torch.split(tensors[i], split_size)]
        
        concatenated_tensor = torch.cat([splitted_tensors[j] for j in range(len(splitted_tensors))], dim=1) # Concatenate the split tensors along dimension 0
        return concatenated_tensor


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(32, 4, 8, 56, 74)
__output__  = m(x1).shape[0] == x1.shape[0]

