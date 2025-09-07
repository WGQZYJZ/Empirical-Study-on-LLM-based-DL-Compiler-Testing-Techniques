class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
         v1  = torch.split(x1, 64, dim=2) # Split the input tensor into several tensors along dimension 2 with size of each tensor being 64 
         v2  = torch.split(v1[0], [32] * (len(v1)), dim=0)[-1]
         v5  = torch.split(x1, 8) # Split the input tensor into several tensors along dimension 1 with size of each tensor being 8
         v6  = x1
         return v1 + v5 + [torch.cat([v2 for i in range(len(v1))], dim=0)] + torch.cat([v3[i] * 7 + v4[i][j] for j, v3 in enumerate(v6) for i in range(8)], dim=-1)
