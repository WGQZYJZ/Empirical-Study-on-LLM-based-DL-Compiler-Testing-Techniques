
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, dim=0, maxlen=15, maxbatch=-1):
        super().__init__()
        self.scale = 1 / math.sqrt(dim) # sqrt of the dimension of the key/query vectors
        self.proj_num = 2 * maxlen + maxbatch
        self.W1 = torch.nn.Linear(dim, proj_num)
        self.W2 = torch.nn.Linear(proj_num, dim)
 
    def forward(self, q, k, v):
        batch, seq_len, dim = q.shape
        dim  //= batch * seq_len
        batch, max_len, seq_len  *= dim
        # We have maxbatch*maxlen/2 vectors, and we only need one vector for attention weights
        scale  //= self.scale
        batch, max_len  //= maxbatch * maxlen
        q    = q[:, :, :dim]
        k    = k[:, :, :dim]
        v    = v[:, :, :dim]
 
        # (batch*seq_len, dim)
        q     = torch.cat([q[:, :, 0], q[:, :, -1]], dim=-1)
        # (batch*seq_len/2, dim)
        k     = torch.cat([k[:, :, 0:maxlen//2], k[:, :, maxlen//2:]], dim=-1)
        # (batch, seq_len, dim)
        attn  = torch.bmm(q, k.permute(0, 2, 1)) / scale
 
        # (batch*seq_len/2, batch*dim)
        W     = self.W1(attn).reshape(-1, self.proj_num, dim)
        # (batch, seq_len/2, batch*dim)
        proj  = torch.bmm(self.W2(attn), v)
 
        # Reshape to original shape
        return proj.permute(0, 2, 1).contiguous()
 
    def __repr__(self):
        return self.__class__.__name__ + ' (' + str(self.proj_num) + ')'


# Initializing the model
m = ScaledDotProductAttention()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
