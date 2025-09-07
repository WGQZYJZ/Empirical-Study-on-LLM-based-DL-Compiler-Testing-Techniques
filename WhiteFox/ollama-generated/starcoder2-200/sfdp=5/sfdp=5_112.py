
class TransformerModel(torch.nn.Module):
    def __init__(self, embedding_dim, num_heads):
        super().__init__()
 
        self._embedding = torch.nn.EmbeddingBag(vocab_size, embedding_dim)  # Create the EmbeddingBag layer for word embedding
        self._encoder  = EncoderLayer()
        self._decoder  = DecoderLayer()
        self._linear   = torch.nn.Linear(embedding_dim, vocab_size)
 
    def forward(self):
        v1  = self._embedding(input) # Use the EmbeddingBag layer to generate word embedding
        v2  = v1.transpose(-2, -1).unsqueeze(1) # Reshape and unsqueeze the word embedding vector into the shape [batch_size x encoder sequence length x num_heads x embedding dimension]
        v3  = self._encoder(v2) # Encode each block in the EncoderLayer
        v4  = self._decoder(v3) # Decode each block in the DecoderLayer
        v5  = torch.nn.functional.linear(v4, self._linear.weight, self._linear.bias) # Compute the output of linear layer as the final output
        return v5
