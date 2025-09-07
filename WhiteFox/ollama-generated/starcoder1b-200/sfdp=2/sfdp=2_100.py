
class Model(torch.nn.Module):
    def __init__(self, embedding_dim, hidden_dim):
        super().__init__()
        self.embedding = torch.nn.Embedding(num_embeddings=vocab_size, embedding_dim=embedding_dim)
        self.encoder = Encoder(hidden_dim, num_layers)

    def forward(self, x1, x2):
        # Embedding layer
        embedded = self.embedding(x1).view(-1, embedding_dim)  # Shape: [batch, sequence length, emb_dim]
        hidden = self.encoder(embedded, x2)  # Shape: [batch, num_layers * num_directions, sequence length, enc_dim]

        return hidden

# Initializing the model
m = Model(100, 300)

