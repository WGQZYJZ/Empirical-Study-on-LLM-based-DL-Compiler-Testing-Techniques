
class TransformerModel(torch.nn.Module):
    def __init__(self, input_size=30000, hidden_size=512, nlayers=4, dropout_p=0.1):
        super().__init__()
        self.nlayers = 4
 
        # We pass the number of tokens to the embedding and decoder, which 
        # in turn creates one embedding for each token in our vocabulary. 
        self.encoder = torch.nn.Embedding(input_size, hidden_size)
        self.attn = torch.nn.MultiheadAttention(hidden_size=512, num_heads=8)
 
        # The linear layer that takes the attention output and passes it to the 
        # final decoder layer. It is used to transform each token into a score 
        # that represents how much attention it should get from other tokens.
        self.decoder = torch.nn.Linear(hidden_size, input_size)
 
    def forward(self, query):
        batch_size  = query.shape[0]
 
        # We pass the query through the embedding layer, then we apply dropout 
        # to each token and run each token through the multiheadattention layer.
        emb = self.encoder(query).dropout_(p=0.1) 
        attn_output, attn_weights  = self.attn(emb, emb, emb)
 
        # Now that we have the attention weights for each token in our sequence 
        # of tokens, we pass these weights to the decoder as additional contextual
        # information. Then we apply dropout and finally run the result through
        # a linear layer which takes in each token’s representation.
        dec = self.decoder(attn_output)
        dec  = torch.dropout_(dec, p=0.1)
 
        return dec


m = TransformerModel()
