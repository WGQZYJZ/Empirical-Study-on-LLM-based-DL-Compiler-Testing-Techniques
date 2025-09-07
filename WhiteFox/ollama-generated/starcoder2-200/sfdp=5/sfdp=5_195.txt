
class Attention(torch.nn.Module):
    def __init__(self, embedding_dim=768, n_head=12, attn_dropout=0.1, dropout=0.1):
        super().__init__()
        self.n_head = n_head
        self.scaling = 1/math.sqrt(embedding_dim//self.n_head)
 
        self.query_proj = torch.nn.Linear(embedding_dim, embedding_dim)
        self.key_proj = torch.nn.Linear(embedding_dim, embedding_dim)
        self.value_proj = torch.nn.Linear(embedding_dim, embedding_dim)
        self.attn_dropout = torch.nn.Dropout(attn_dropout)
 
    def forward(self, query: torch.Tensor):  # type: ignore
        batch_size, seq_len, emb_size = query.shape
        assert emb_size == self.n_head * self.scaling**2
 
        qkv = self.query_proj(query).view(batch_size, -1, self.n_head, 3*emb_size//self.n_head)
        k, v = torch.unbind(qkv, dim=-1) # type: ignore
        qkv_transpose = torch.einsum('b i h n, b j k m -> b h (n o) (j o)', [k.transpose(-2,-3),v]).view(batch_size*self.n_head, -1, emb_size//self.n_head*2)
 
        attn_mask = torch.triu(torch.ones((seq_len-1, seq_len-1)), diagonal=0).bool() # type: ignore
        attn_weight  = torch.softmax(qkv_transpose @ qkv_transpose.permute(1, 2) / self.scaling, dim=-1) # Compute the dot product of the query and key, followed by a softmax operation to compute attention weights 
        attn_weight = torch.dropout(attn_weight, dropout, True) # Apply dropout
 
        attn_weight  = torch.triu((attn_weight-torch.ones_like(attn_weight)).mul_(self.n_head).ceil().div_(self.n_head).bool(), diagonal=1)+torch.zeros((batch_size*self.n_head, seq_len, seq_len)) # mask out self attention
        output  = attn_weight @ qkv_transpose  # Compute the dot product of these attention weights and the value
        output = torch.einsum('b (h n o) m d -> b h o m', [output, v]).view(batch_size*self.n_head//2, -1, emb_size//self.n_head*2).view(batch_size, self.n_head, seq_len, emb_size//self.n_head)
        output  = torch.einsum('b h o (m d)-> b h o m', [output, v]).view(batch_size, -1, emb_size).contiguous()
        return output
 
model = Attention()


# Inputs to the model
x1 = torch.randn(2, 64)