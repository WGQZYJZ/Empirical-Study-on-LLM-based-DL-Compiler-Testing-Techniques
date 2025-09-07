
class TransformerModel(torch.nn.Module):
    def __init__(self, ninp=512, nhead=8):
        super().__init__()
        self.embed = torch.nn.Embedding(203, 512) # Input embedding (word embeddings for each token in the input sequence)
        self.pos_encoder = PositionalEncoding() # Applies positional encoding
        self.encoder = torch.nn.TransformerEncoderLayer(d_model=ninp, nhead=8) # Transformer encoder layer
        self.decoder = torch.nn.TransformerDecoderLayer(d_model=ninp, nhead=nhead)
 
    def forward(self, x):
        emb  = self.embed(x).permute([1,0,2])
        posenc  = self.pos_encoder(emb).permute([1,0,2])
        enc  = self.encoder(posenc)
        dec  = self.decoder(emb, enc) # Decoder layer
        return dec

# Initializing the model
m = TransformerModel()

