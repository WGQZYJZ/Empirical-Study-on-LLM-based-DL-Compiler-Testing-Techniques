
class TransformerModel(torch.nn.Module):
    def __init__(self):
        super().__init__()

        self.embedding = torch.nn.Embedding(vocab, embedding)
 
        self.position_enc = PositionalEncoding(embedding, dropout=0.5)
 
        # Transformer layers
        self.encoder  = EncoderDecoderModel(N, vocab, d_model, heads)
        
        self.decoder = DecoderOnly(N, vocab, d_model, heads)
 
    def forward(self, src):
        output  = self.embedding(src) # Embed the source tensor
        posi_encoded = self.position_enc(output) # Compute the positional encoding to the embedding
        enc_out = self.encoder(posi_encoded, src, src, True) # Encode the embedding with source as input
        dec_out  = self.decoder(output, src, src, False) # Decode and output to the embedding 
        return dec_out

# Initializing model
m = TransformerModel()
 
# Inputs to the model
src = torch.randn(10, 256).long()
