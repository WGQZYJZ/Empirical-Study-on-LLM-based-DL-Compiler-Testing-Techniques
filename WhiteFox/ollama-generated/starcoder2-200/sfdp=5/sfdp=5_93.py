
class TransformerModel(torch.nn.Module):
    def __init__(self, emb_dims=[512], nlayers=6, ff_hiddensize=2048, nheads=8):
        super().__init__()
 
        self.emb = torch.nn.Embedding(vocab_sz, emb_dims[-1])  # Word embedding layer
        encoder_layer = nn.TransformerEncoderLayer(d_model=emb_dims[0], nhead=nheads)  # Define the transformer encoder
        self.transformer_encoder = nn.TransformerEncoder(encoder_layer, num_layers=nlayers)
 
    def forward(self, x1):
        v1  = self.emb(x1).transpose(-2,-3)
 
        mask = self.transformer_encoder._generate_square_subsequent_mask(v1.size(-3))  # Generate a mask for the sequence length of the query and key
        mask = mask == False
        attn_mask = -torch.ones_like(v1[0,0]).to("cuda") + float(not mask)
 
        v2 = self.transformer_encoder._norm1(v1)  # Normalize the output of the encoder layer
        v3 = self.transformer_encoder._layers[-1](v2)  # Compute the dot product of the dropout output and the value
        return v3
# Initializing the model
m  = Model()

