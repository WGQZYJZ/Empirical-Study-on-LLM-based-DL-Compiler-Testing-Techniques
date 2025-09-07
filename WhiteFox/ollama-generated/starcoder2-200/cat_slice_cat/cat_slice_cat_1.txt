
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1s):
        v1 = torch.cat(x1s, dim=0) 
        v2 = v1[:, 9375:68547] # 9375 is just a random number and 68547 is the largest int
        v3 = x1s[0][v2].reshape(-1).mean() 
        return torch.erf(v3) + 1

# Initializing the model
m = Model()

