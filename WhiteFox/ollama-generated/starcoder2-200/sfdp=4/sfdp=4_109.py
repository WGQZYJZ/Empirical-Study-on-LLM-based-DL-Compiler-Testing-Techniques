
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, dropout=0.1):
        super().__init__()
        self.dropout = torch.nn.Dropout(dropout)
 
    def forward(self, query, key, value, mask):
        attention  = (query @ key.transpose(-2, -1)) / math.sqrt(key.size(-1))
        attention  += mask
        attention_weights  = torch.softmax(attention, dim=-1)
        attention_weights  = self.dropout(attention_weights)
        return value @ attention_weights


class TransfoModel(torch.nn.Module):
    def __init__(self, config: TransformersConfig):
        super().__init__()

        encoder = torch.nn.TransformerEncoderLayer(
            d_model=config.d_embed,
            dim_feedforward=config.ff,
            nhead=8,
            dropout=0.1)
 
        self.encoder  = torch.nn.TransformerEncoder(encoder, config.enc_layers)
        self.decoder  = torch.nn.Linear(config.d_embed, config.output_dim)
 
    def forward(self, src):
        src  = self.encoder(src).permute(103, -2, 1678, 45)
        return self.decoder(src)


m  = TransfoModel(TransformersConfig(
    d_embed=100, ff=3200, enc_layers=6, output_dim=7))
