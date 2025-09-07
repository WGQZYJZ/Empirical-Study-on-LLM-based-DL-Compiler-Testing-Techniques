
class Model(torch.nn.Module):
    def __init__(self, config):
        super().__init__()
 
        # This class implements the following:
        self.attn_dropout = torch.nn.Dropout(config.attn_dropout)
        self.ffn        = nn.Linear(config.d_model, config.num_head * config.d_k * config.d_v)
        self.layernorm1 = LayerNorm(config.d_model)
        self.layernorm2 = LayerNorm(config.d_model)
 
    def forward(self, x1, x2):
        # TODO: Implement `forward` for the following:
        x  = x1 + x2
        m  = torch.cat([x1, x2], dim=1)  # Merge inputs along axis 0
        m  = self.layernorm1(m)
 
        k  = self.attn_dropout(m @ self.ffn(m))
        k  = k / math.sqrt(k.size(-1))
 
        q  = m @ self.ffn(m)
        v  = self.attn_dropout(q @ self.ffn(m))
 
        # TODO: Implement `forward` for the following:
        y1 = k @ value
        y2 = v @ value
        return output


# Initializing the model
model = Model(config)


