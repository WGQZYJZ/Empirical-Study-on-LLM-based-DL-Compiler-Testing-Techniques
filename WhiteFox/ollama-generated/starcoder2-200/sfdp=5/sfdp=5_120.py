
class TransformerModel(nn.Module):
    def __init__(self, nhead=4, num_layers=2):
        super().__init__()
        self.encoder = nn.TransformerEncoderLayer(d_model, nhead)
        self.encoder_norm  = nn.LayerNorm(d_model)
 
        self.decoder  = nn.TransformerDecoderLayer(d_model, nhead)
        self.decoder_norm  = nn.LayerNorm(d_model)
 
    def forward(self, src):
        return self._forward(src)
 
    def _forward(self, src):
        return torch.nn.functional.gelu((self.encoder_norm(src + self.decoder_norm(self.encoder(src)))))
 
m  = TransformerModel()


# Initializing the model