
class TransformerModel(nn.Module):
    def __init__(self, embedding_dim = 32, hidden_dim = 64, vocab_size = 51095):
        super().__init__()
 
        # Word Embedding
        self.word_embeddings = nn.Embedding(vocab_size, embedding_dim)

        # Transformer
        encoder_layer = nn.TransformerEncoderLayer(embedding_dim, hidden_dim // 4)
        self.transformer_encoder = nn.TransformerEncoder(encoder_layer, num_layers=6)
 
        # Linear Layer
        self.linear1 = nn.Linear(hidden_dim, vocab_size)

    def forward(self, input):
        embedded = self.word_embeddings(input)  # Embedding
        output = self.transformer_encoder(embedded)   # Transform
        logits = self.linear1(output[:, -1])    # Linear Layer
        return logits

# Initializing the model
model  = TransformerModel()

