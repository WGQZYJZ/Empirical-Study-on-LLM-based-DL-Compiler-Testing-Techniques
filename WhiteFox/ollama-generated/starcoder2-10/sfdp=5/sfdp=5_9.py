
class TransformerBlock(torch.nn.Module):
    def __init__(self, dim=768, num_heads=12, mlp_dim=3072, dropout = 0.5):
        super().__init__()
 
        self._att = torch.nn.MultiheadAttention(dim,num_heads)
        
        self._mlp = torch.nn.Sequential(
            torch.nn.Linear(in_features= dim, out_features= mlp_dim),
            torch.nn.GELU(), # or torch.nn.ReLU()
            torch.nn.Dropout(dropout))
 
    def forward(self, x):
        y  = self._att(x)[0] + x   # query @ key.transpose(-2,-1)
        return self._mlp(y), y


class Model(torch.nn.Module):
    def __init__(self, d_model=768): 
        super().__init__()
 
        self.encoder = torch.nn.Sequential(*[TransformerBlock() for _ in range(5)])
 
    def forward(self,x):
        y  = self._att(x)[0] + x   # query @ key.transpose(-2,-1)
        return y


# Initializing the model and its components
m = Model().cuda()
 
# Inputs to the model
x = torch.randn(8, 768).cuda()
 
 