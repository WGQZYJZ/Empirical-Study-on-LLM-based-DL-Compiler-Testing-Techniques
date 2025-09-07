
class Attention(torch.nn.Module):
    def __init__(self, dim=768, inv_scale = 12.0):
        super().__init__()
        self.query  = torch.nn.Linear(dim, dim)
        self.key    = torch.nn.Linear(dim, dim)
        self.value  = torch.nn.Linear(dim, dim)
        self.attn_drop   = torch.nn.Dropout(0.1)
        self.proj        = torch.nn.Linear(dim * 3, dim)
 
    def forward(self, x):
        q  = self.query(x).permute(1, 2, 0) # (batch_size, n, dim)
        k  = self.key(q) 
        v  = self.value(k)
        scaled_dot_product  = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(dim)
        attention_weights   = scaled_dot_product.softmax(dim=-1) # (batch, num_heads, n, k), where k is the length of keys/queries
        proj  = self.proj(torch.cat((q, v * attention_weights, torch.zeros(*q.shape)), dim=2))
        return proj[:, :, :768] + proj[:, :, 768:]
 
 # Initializing the model
 m = Attention()

 # Input tensors to the model
 x1   = torch.randn(30, 512)  
 x2   = torch.randn(30, 512)
 __output__  = m(x1).matmul(x2)
 
