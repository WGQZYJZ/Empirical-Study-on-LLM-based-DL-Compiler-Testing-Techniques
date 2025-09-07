
class Model(torch.nn.Module):
    def __init__(self, embedding_dim=128, hidden_size=3072, num_heads=16, num_layers=4):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim)  # Embed the vocabulary as vectors of a given dimension into a dimention of `embedding_dim` for each word in the corpus
        self.position_encoding = PositionEncoding(embedding_dim)
        self.attention = MultiHeadAttention(
            embed_dim=embedding_dim, hidden_size=hidden_size, num_heads=num_heads, dropout=dropout_p)
        self.linear = nn.Linear(hidden_size, vocab_size)  # Output the embeddings of a word as it is in the corpus and into a new vocabulary of size `vocab_size`
        
    def forward(self, inputs):
        input_embed = self.embedding(inputs)  # Embed a given word
        
        pooled_output, _ = torch.nn.functional.adaptive_max_pool1d(input_embed, (inputs.shape[-2] // attention.num_attention_heads))  # Apply max pooling to the embeddings

        position_embeddings = self.position_encoding(inputs)  # Compute a new representation for each word using its current embedding and the corresponding position
        
        h = torch.cat([input_embed, position_embeddings], dim=-2)  # Merge all embeddings into one
        h = self.attention(h, h)  # Apply attention to merge two representations
        
        return self.linear(self.dropout(torch.nn.functional.relu(h)))  # Softmax the dot product and apply dropout on it


# Initializing the model
m = Model()

