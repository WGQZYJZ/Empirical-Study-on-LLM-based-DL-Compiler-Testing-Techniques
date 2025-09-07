
class AttentionBlock(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
 
        # This is the "Attention Block" in the figure above, which has 3 components:
        # - A scaled dot-product attention mechanism
        # - An attention weight normalization
        # - A feedforward network with ReLU activation
        self.norm1 = torch.nn.LayerNorm(dim)
        self.norm2 = torch.nn.LayerNorm(dim)
 
        self.attn_weights  = torch.nn.Linear(dim, dim // 8) 
        self.ffw  = torch.nn.Sequential(
            torch.nn.Linear(dim, dim * 4), 
            torch.nn.ReLU(),
            torch.nn.Linear(dim * 4, dim)
        )
 
    def forward(self, x):
        query, key, value = self.get_components(x)
 
        scaled_dot_product  = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(key.size(-1))
        attn_weights  = self.attn_weights(scaled_dot_product).softmax(dim=-1)
        output  = attn_weights.matmul(value)
        ff_output  = self.norm2(self.ffw(x + output)).relu()
 
        return self.norm1(x + ff_output), ff_output
 
    def get_components(self, x):
        batch_size  = x.shape[0]
        return (
            self.norm1(x).view(batch_size * -1, self.get_dim(x)).view(-1, 256, int(self.get_dim(x) / 8)), 
            key=x, value=x, 
        )
 
    def get_dim(self, x):
        return x[0].shape[-1]


# Initializing the model and getting its parameters
ab = AttentionBlock(256)
params  = ab.parameters()
 
# Inputs to the model 
query = torch.randn(8, 32, 256)
key   = value = torch.randn(4, 1024, 256)
__output__, ff_output  = ab(query)


