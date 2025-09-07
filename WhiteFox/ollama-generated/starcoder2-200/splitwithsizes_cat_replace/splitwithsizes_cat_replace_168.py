
class Model(torch.nn.Module):
    def __init__(self, split_sizes=5, dim=-1):
        super().__init__()
 
    def forward(self, x0):
        # Initializing some variables
        output  = torch.zeros(24, 3)
        
        splitted_tensor = []
        for i in range(len(split_sizes)):
            splitted_tensors[i] = self._split(input_tensor, [1]*int(dim), dim)
 
        concatenated_tensor  = self._cat([splitted_tensor[i][j] for i in range(4)], dim)
        #return True
        return output
 
    def _split(self, tensor, sizes, dim):
        return torch.split(tensor, splitSizes, dim=dim)
 
    def _cat(tensors, dim=-1):
        return torch.cat([tensor[i] for i in range(len(splitSizes))], dim=dim)


# Initializing the model 
m = Model(split_sizes=[4]*4).to('cuda')

# Inputs to the model
x0 = torch.randn(3, 27, device='cuda:0').split(int(2*9))
