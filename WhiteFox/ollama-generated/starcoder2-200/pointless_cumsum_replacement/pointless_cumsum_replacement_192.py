
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.cumsum  = torch.Tensor([arg1, arg2])
 
    def forward(self, x1):
        v1  = torch.full([3072, 64], 1., device=device) 
        v2  = torch.tensor(v1).to(torch.float)
        v3  = self.cumsum
        v4  = v2 + v3 # Add the cumulative sum of the elements along dimension `1` to each row of the tensor with the specified dtype and device
        return v4


# Initializing the model