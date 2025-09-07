
class TransformerModel(torch.nn.Module):
    def __init__(self, ntoken=201438, d_model=512, dropout=0.1)
        super().__init__()
        self.encoder = torch.nn.Embedding(ntoken, d_model)
        encoder_layer = nn.TransformerEncoderLayer(d_model, 8, dropout) # Addition of layers to the Transformer encoder
        self.transformer_encoder = torch.nn.TransformerEncoder(encoder_layer, num_layers=6)

        self.fc = nn.Linear(d_model * 3072, d_model*3072)
 
    def forward(self, inp):
            emb  = self.encoder(inp).transpose(1, -1)
            v1   = self.transformer_encoder(emb) 
            v4   = torch.softmax(v1[-9:,:,:], dim=-2)
            v5   = v4 @ torch.randn(3072*d_model, 3072*d_model).float() # Multiply the result of softmax by a random matrix
            v6   = v1[-8:, :] * v5.transpose(-2,-1)  
            return (v6, self.fc(v4)) # Return output of transformer encoder


# Initializing the model
m  = TransformerModel()



# Inputs to the model
x  = torch.randint(low=0, high=201438-1, size=(5,), dtype=torch.int64)
__output__  = m(x)

