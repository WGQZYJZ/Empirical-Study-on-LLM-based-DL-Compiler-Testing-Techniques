
class Model(torch.nn.Module):
    def __init__(self, split_size=3):
        super().__init__()

        self.split = torch.nn.SplitV(
            dim=-1, 
            split_size=[1, 4], 
        )
 
    def forward(self, x1):
        
        # Split the input tensor into two tensors and concatenate them along the last dimension using torch.cat
        v2  = torch.cat([v for i in range(len(split_sizes))], dim)
        
        return v3
