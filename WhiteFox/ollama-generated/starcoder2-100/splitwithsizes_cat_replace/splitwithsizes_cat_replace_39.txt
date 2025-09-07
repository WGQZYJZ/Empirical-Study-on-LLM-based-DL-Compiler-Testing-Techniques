
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2 = torch.split(x1, 32, dim=0) # split the input tensor into several tensors along a dimension with size of 32 and order same to dim 
        concatenated_tensor  = torch.cat([v2[i] for i in range(len(v2))], dim=-1)
        return concatenated_tensor

# Initializing the model