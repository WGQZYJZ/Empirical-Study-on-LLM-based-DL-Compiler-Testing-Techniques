
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()
        self.mat = torch.Tensor([
            [2., 3.], 
            [-0.5, -0.7] 
        ])
    
    def forward(self, x1):
        v1  = torch.addmm(x1, self.mat[:, None], self.mat[None]) # The resulting tensor should be of size (batch_size, dim)
        v2  = torch.cat([v1[..., :3]], dim=dim)                  # The resulting tensor should be of the same shape as that of x1, except in one dimension where it is larger by 5
        return v2


# Initializing the model