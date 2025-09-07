
class Transformer(torch.nn.Module):
    def __init__(self, d_model=1024, nhead=8, num_encoder_layers=6, num_decoder_layers=6, dropout=0.1):
        super().__init__()
        self.encoder = torch.nn.TransformerEncoder(torch.nn.TransformerEncoderLayer(d_model=d_model, nhead=nhead), num_encoder_layers)
        self.decoder = torch.nn.TransformerDecoder(torch.nn.TransformerDecoderLayer(d_model=d_model, nhead=nhead), num_decoder_layers)
 
    def forward(self, x1):
        v1  = self.encoder(x1) # Apply encoder
        v2  = self.decoder(x1) # Apply decoder
        return v1


# Initializing the model
m  = Transformer()
 
# Inputs to the model
x1  = torch.randn(4, 60, 837)

__output__  = m(x1)

