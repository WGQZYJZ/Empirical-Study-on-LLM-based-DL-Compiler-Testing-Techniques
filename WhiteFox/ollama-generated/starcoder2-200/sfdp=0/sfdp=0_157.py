
class Transformer(torch.nn.Module):
    def __init__(self, embedding_dim=768, hidden_dim=3072, output_dim=1536, num_heads=12, num_layers=12, dropout_prob=.1, max_len=128):
        super().__init__()
        self.embedding = torch.nn.Embedding(vocab_size + 1, embedding_dim)
        encoder_layer = TransformerEncoderLayer(
            d_model=hidden_dim // num_heads, 
            nhead=num_heads, 
            dim_feedforward=4 * hidden_dim, dropout=.1)
        self.transformer_encoder = TransformerEncoder(encoder_layer, num_layers=num_layers)
    
    def forward(self, x):
        # Pass the input (x) through the model encoder and decoder
        x  = self.embedding(x)
        return self.transformer_encoder(x)
# Initializing the model
model1  = Transformer()
 
# Inputs to the model
inputs1 = torch.randint(0, vocab_size + 1, (batch_size,), dtype=torch.long)
__output1__ = model1(inputs1)


