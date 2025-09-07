
class Attention(torch.nn.Module):
    def __init__(self, embed_dim, num_heads=4):
        super().__init__()
 
        self.embed_dim = embed_dim
        self.num_heads  = num_heads
        self.head_dim  = embed_dim // num_heads
        assert (self.head_dim * num_heads == self.embed_dim)
        
        self.scale  = torch.rsqrt(torch.tensor(self.head_dim))
        self.query = torch.nn.Linear(self.embed_dim, self.num_heads*self.head_dim) # linear layer to project query features into projection space
        self.key   = torch.nn.Linear(self.embed_dim, 4*self.head_dim) # 4 = sqrt of the number of attention heads
        self.value = torch.nn.Linear(self.embed_dim, 4*self.head_dim) # 4 = sqrt of the number of attention heads
        
    def forward(self, query=None):
 
        qk_v  = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        qk_v  = qk_v + attn_mask 
        # Add the attention mask to the scaled dot product
        attn_weight  = torch.softmax(qk_v, dim=-1)
        
        attn_weight  = torch.dropout(attn_weight, dropout_p, True)
        output  = attn_weight @ value 
        return output


# Initializing the model
m  = Attention(3200)
__output__  = m() # __output__ is a torch.Tensor of shape (batch size x sequence length).

