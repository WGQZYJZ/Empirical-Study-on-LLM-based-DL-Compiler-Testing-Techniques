
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v0 = torch.split(x1, [256], dim=3)  # Split the input tensor into two tensors with length 256 along dimension 3
        v1 = torch.cat([v0[i] for i in range(len(v0))], dim=3) 
        return v1


