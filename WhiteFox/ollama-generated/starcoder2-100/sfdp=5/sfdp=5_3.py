
class MyTransformerModel(torch.nn.Module):
    def __init__(self,
                 dim_model=256,
                 num_layers=8,
                 max_seq_len=1073741824):
        super().__init__()
 
        self._encoder  = torch.nn.TransformerEncoderLayer(d_model=dim_model,
                                                          nhead=8)
        
        self._query = torch.nn.Linear(in_features=max_seq_len,
                                      out_features=3072)
        self._key   = torch.nn.Linear(in_features=max_seq_len,
                                      out_features=3072)
        self._value = torch.nn.Linear(in_features=max_seq_len,
                                      out_features=dim_model * 8)
   
        self.pos_encoder = PositionalEncodingLayer(embedder=self._encoder)

        self._norm1 = LayerNorm(normalized_shape=[3072]) 
        self._norm2 = LayerNorm(normalized_shape=[4*max_seq_len])
 
    def forward(self, query):
        key   = self._key  (query)
        value = self._value(query)
 
        k = self.pos_encoder(key)
        q = self.pos_encoder(query)
 
        mask  = torch.tril(torch.ones([k.size(-2), k.size(-1)],
                                     device=query.device))
        k  = self._norm1(k)
        q, _  = torch.max(q, dim=-1)
        q  = self._norm1(q)
        
        v1  = self._encoder(q)
        v2  = self._query(v1).transpose(-2, -1)
        v3  = k * v2
        attn_mask  = (1.0 - mask.masked_fill_(mask == False, float("-inf"))
                      + mask.masked_fill_(mask != False, -float("Inf")))
        v4 = torch.softmax(attn_mask, dim=-1)

        v5 = self._norm2(v4  @ value).transpose(-3, -2)
        
        v6 = torch.erf(v5 + torch.randn((query.size(-1), query.size(-1)),
                                        device=query.device))
        return v6
