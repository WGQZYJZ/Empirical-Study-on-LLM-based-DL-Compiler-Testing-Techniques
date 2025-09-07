
class Model(torch.nn.Module):
    def __init__(self, embed_dim, num_heads, depth):
        super().__init__()
        self.embed_dim = embed_dim
        self.num_heads = num_heads
        self.depth = depth
 
        self.q = torch.nn.Linear(embed_dim * 2, num_heads * depth)
        self.k = torch.nn.Linear(embed_dim * 2, num_heads * depth)
        self.v = torch.nn.Linear(embed_dim * 2, num_heads * depth)
 
    def forward(self, x):
        qk = torch.cat([self.q(x), self.k(x)], dim=-1)
        output = (qk @ self.w) + b
        return output
 

 # Initializing the model
m = Model(embed_dim=1024, num_heads=32, depth=64)
 
 # Inputs to the model
x  = torch.randn(1, 3, 512, 8)
