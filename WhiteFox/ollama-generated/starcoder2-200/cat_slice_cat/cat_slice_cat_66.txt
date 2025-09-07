
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x0):
        v1  = torch.cat([x0[i] for i in range(len(x0))], dim=1) # Concatenate input tensors along dimension 1
 
        size = x0[4].size()[1]
        v2  = v1[:, :int(torch.tensor(9223372036854775807))]
        v3  = v2[:, :size]
        
        return torch.cat([v1, v3], dim=1)
