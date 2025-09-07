
class TransformerModel(torch.nn.Module):
    def __init__(self,
                 d_model: int = 1280,
                 num_layers=6,
                 dropout=0.1,
                 max_len: int = 512) -> None:
        super().__init__()
        self.d_model = d_model
        self.embed = torch.nn.Embedding(
            d_model + 1, d_model)
 
        self.pos_encoder = PositionalEncoding(d_model, dropout=dropout)
        encoder_layers = EncoderLayer(d_model, dropout=dropout)
        
        # Encoder layers
        encoder_layer  =  nn.ModuleList()
        for _ in range(num_layers):
            encoder_layer.append(encoder_layers)
 
        self.encoder = nn.Sequential(*encoder_layer)
 
    def forward(self, query: torch.Tensor, attn_mask=None) -> torch.Tensor:
        batch_size  =query.shape[0] # shape: (batch,)
        length      = query.shape[-1] # shape: ()
        position    = torch.arange(length).expand((batch_size, length)).to(query.device)
 
        qk = query @ query.transpose(-2, -1) / math.sqrt(self.d_model) + attn_mask
        attn_weights = torch.softmax(qk, dim=-1)
        output       = attn_weights @ query
 
        return output

m  = TransformerModel()

