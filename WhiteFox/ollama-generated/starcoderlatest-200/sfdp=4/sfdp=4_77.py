
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_q = torch.nn.Linear(256, 1024) 
        self.attn_k = torch.nn.Linear(1024, 1024) 
        self.attn_v = torch.nn.Linear(1024, 1024) 
        self.ffn = torch.nn.Sequential(
                torch.nn.LayerNorm(1024), 
                torch.nn.GELU(), 
                torch.nn.Linear(1024, 1024),
        )
 
    def forward(self, x):
        attn_q  = self.attn_q(x)
        attn_k  = self.attn_k(x) 
        attn_v  = self.attn_v(x) 
        ffn_output = self.ffn(attn_q)
 
        return attn_weight
# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(8, 256, 64, 64) 
