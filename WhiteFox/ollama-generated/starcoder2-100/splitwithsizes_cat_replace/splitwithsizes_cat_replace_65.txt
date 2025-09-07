
class Model(torch.nn.Module):
    def __init__(self, dim=0):
        super().__init__()
 
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        
        self._splitdim = dim
 
    def forward(self, x1):
        # split input tensor by self._splitdim and perform concatenation along the same dimension
        split_tensors = torch.split(x1, split_sizes=[256], dim=self._splitdim) 
        concatenated_tensor  = torch.cat([split_tensors[i] for i in range(len(split_sizes))], self._splitdim)
        
        return self.conv(concatenated_tensor)


# Initializing the model