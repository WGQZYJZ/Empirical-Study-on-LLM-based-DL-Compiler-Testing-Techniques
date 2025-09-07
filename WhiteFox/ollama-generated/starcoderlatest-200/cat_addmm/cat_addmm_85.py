
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.addmm(x1, torch.eye(3).unsqueeze(dim), torch.eye(8).unsqueeze(dim))
        v2 = torch.cat([v1], dim)
        return v2
 
 # Initializing the model
m = Model(0)
 
 # Inputs to the model
 x1 = torch.randn(1, 3, 64, 64)
 