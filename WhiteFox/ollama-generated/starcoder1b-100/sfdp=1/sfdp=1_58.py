
class Model(torch.nn.Module):
    def __init__(self,
                 num_attention_heads: int = 8,
                 d_k: int = 64,
                 d_v: int = 64,
                 dropout_p: float = 0.1):
        super().__init__()
        self.query = torch.nn.Linear(d_k, num_attention_heads * d_v)
        self.key = torch.nn.Linear(d_k, num_attention_heads * d_v)
        self.value = torch.nn.Linear(d_v, num_attention_heads * d_v)
        self.dropout = torch.nn.Dropout(p=dropout_p)
 
    def forward(self, query: Tensor, key: Tensor):
        v  = self.value(query).unsqueeze(dim=-1) # B x K x D -> (B*K) x 1 x D
        k  = self.key(key).transpose(-2, -1).contiguous()    # (B*K) x D -> (B*K) x K x D
        q  = self.query(query).contiguous()           # B x Q x D -> B x Q x K
        scaled_q  = q / (self._sqrt_d * torch.sqrt(k)) # (B*Q) x K/sqrt(D) x D -> B*Q x K/sqrt(D)
        softmax_qk = F.softmax(scaled_q, dim=-1) # (B*Q) x K/sqrt(D) -> B*Q x K/sqrt(D) x 2^{d-k}
        dropout_qk = F.dropout(softmax_qk, p=self.dropout_p) # (B*Q) x K/sqrt(D) -> B*Q x K/sqrt(D) x 2^{d-k}

        return self.dropout(dropout_qk).matmul(v)

# Initializing the model
m = Model()
