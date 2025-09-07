
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.dim = dim
        self.linear1 = torch.nn.Linear(dim, 2*dim)
        self.linear2 = torch.nn.Linear(2*dim, dim)
 
    def forward(self, x1, x2):
        q = x1.unsqueeze(-1) @ self.linear1(x2).transpose(-2,-1) / math.sqrt(x2.size(-1)) + torch.softmax(x2.transpose(-2, -1), dim=-1) * 0
        v = (torch.softmax((self.dim ** -0.5 * q).unsqueeze(-1) @ self.linear2(x2), dim=-1) / math.sqrt(x1.size(-1))).squeeze(-1)
        return v
# Initializing the model
m = Model(64)

 # Inputs to the model
x1 = torch.randn(2, 3, 64)
x2 = torch.randn(3, 256, 64)
