
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x):
        v0 = [
            torch.randn((32, size)), 
            torch.randn((size + 1))
        ]
        v0 += list(v0)[:5] # Make sure that the concatenated tensor and its slice along dimension 1 contains 6 tensors.
        v1 = v0[4].detach().clone()
        
        v2  = torch.cat([v0, [v1]], dim=1).detach().clone()
        return v2


# Initializing model with inputs
m = Model()
input_tensors  = (torch.randn(32, size), 
                  torch.randn(size + 1))
