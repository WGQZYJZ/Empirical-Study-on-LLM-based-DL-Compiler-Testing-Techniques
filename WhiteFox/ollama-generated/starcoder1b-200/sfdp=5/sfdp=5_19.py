
class Model(torch.nn.Module):
    def __init__(self, n_head=8, d_k=64, d_v=64, n_layer=2, dropout_p=0.1, attn_dropout_rate=0.5, max_len=30):
        super().__init__()
        self.n_head = n_head
        self.d_k   = d_k
        self.d_v   = d_v
        self.n_layer = n_layer
        self.dropout_p = dropout_p
        self.attn_dropout_rate = attn_dropout_rate
        
        # TODO: Implement the two variables self.query, self.key
        
        self.layers = torch.nn.ModuleList([
            torch.nn.MultiheadAttention(n_head=self.n_head, d_k=self.d_k, d_v=self.d_v, dropout=self.attn_dropout_rate),
        ])
        self.norm1 = nn.LayerNorm(64)
        self.norm2 = nn.LayerNorm(64)
        
    def forward(self, x):
        output = []
        
        for i in range(self.n_layer):
            prev_output = output[-1] if i < (len(output)-1) else None
            
            # TODO: Implement the two lines above
            
            attn = self.layers[i](prev_output, prev_output, prev_output)  # Compute the scaled dot product of the query and key (the two inputs to the previous layer).
            output.append(self.dropout(attn))
        
        return self.norm2(self.linear(torch.cat([x] + output, dim=-1)))


# Initializing the model
m = Model()


