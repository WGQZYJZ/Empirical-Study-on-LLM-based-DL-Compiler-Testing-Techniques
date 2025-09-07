
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, num_heads=8, key_dim=32, attn_dropout_p=0.1):
        super().__init__()
        self.num_heads = num_heads
        self.key_dim   = key_dim
 
        # Parameters of the linear layer (WQ,WK,WV,Wo) for input projection and output projection respectively
        self.lin_q = torch.nn.Linear(32, num_heads * 32)
        self.lin_k = torch.nn.Linear(key_dim, num_heads * key_dim)
        self.lin_v = torch.nn.Linear(32, num_heads * 32)
        self.lin_o = torch.nn.Linear(32, num_heads * 32)
 
        # Parameters of the linear layer for scaling factor
        self.inv_scale_factor = torch.nn.Parameter(torch.tensor([0.078125]))
        
        # Parameter for dropout in softmax and attention module
        self.attn_dropout = torch.nn.Dropout(attn_dropout_p)
    
    def forward(self, q, k, v):
        xq = self.lin_q(q)  # (b, n, d_head * key_dim)
        xk = self.lin_k(k)  # (b, m, d_head * key_dim)
        xv = self.lin_v(v)  # (b, v, d_head * key_dim)
 
        batch_size   = q.shape[0]
        attention    = torch.einsum('... bd, ... bk -> ... bm', xq, xk)  # (b, n, m)
        scaled_attn  = attention / self.inv_scale_factor  # (b, n, m)
        softmax_attn = scaled_attn.softmax(dim=-1)  # (b, n, m)
        dropout_attn = self.attn_dropout(softmax_attn)  # (b, n, m)
        output       = torch.einsum('... bm, ... bk -> ... bd', dropout_attn, xv)  # (b, n, d_head * key_dim)
        output       = output.transpose(-2, -1).contiguous()  # (b, d_head * key_dim, n)
        
        return output
# Initializing the model
m = MultiHeadAttention(num_heads=8, key_dim=32, attn_dropout_p=0.1)


q    = torch.randn(1, 4, 64, 32) # (batch, head, n, d_head * key_dim)
k    = torch.randn(1, 8, 64, 32) # (batch, head, m, d_head * key_dim)
v    = torch.randn(1, 4, 64, 32) # (batch, head, v, d_head * key_dim)
