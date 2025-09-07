
class TransformerModel(torch.nn.Module):
    def __init__(self, num_layers, hidden_dim, attn_heads=8):
        super().__init__()
 
        self.layer = torch.nn.TransformerEncoderLayer(d_model=hidden_dim, nhead=attn_heads) 
        self.decoder  = torch.nn.TransformerDecoder(self.layer, num_layers=num_layers, norm=None)
 
    def forward(self, input):
        # Encoder-only model, with no encoder-decoder layer or output projections.
        return self.decoder(input)[0]


# Initializing the model
model = TransformerModel(
    num_layers  =   1, 
    hidden_dim=256)
 
 
