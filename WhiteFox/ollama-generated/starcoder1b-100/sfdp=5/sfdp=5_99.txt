
class Model(torch.nn.Module):
    def __init__(self, vocab_size):
        super().__init__()
        self.encoder = torch.nn.Embedding(vocab_size, embedding_dim)  # Create an embedding layer for each token in vocabulary
        self.position_encoding = PositionEncoding(embedding_dim)  # Create an embedding layer for each token in vocabulary
        self.attn = Attention()  # Create a Transformer layer with two encoder layers and three linear transformations
        self.mlp = torch.nn.Linear(embedding_dim * 4, vocab_size)  # Create a linear transformation from input to output

    def forward(self, x):
        b_size = x.shape[0]  # Batch size
        seq_len = x.shape[1]  # Sequence length

        pos_x = self.position_encoding[:, :seq_len]  # Get the position encoding for each token in sequence
        pos_x = pos_x.unsqueeze(0).repeat((b_size, 1, 1))  # Append a dimension to every input tensor for batch and time steps

        # Embedding
        x = self.encoder(x)  # Apply an embedding layer to the input sequence
        x = x + pos_x  # Add the position encoding to the embeddings of each token in the sequence

        # Transformer layers
        encoder_layer = torch.nn.TransformerEncoderLayer(d_model=embedding_dim, nhead=nhead, dim_feedforward=dim_feedforward)
        encoder = torch.nn.TransformerEncoder(encoder_layer, num_layers=num_layers)
        x = encoder(x)  # Apply an encoder layer to the input sequence

        # Linear transformation
        x = x.contiguous().view(-1, embedding_dim * 4)  # Unpack the data in batches to form a flat vector
        x = self.mlp(x)  # Perform a linear transformation on the flattened batch of tokens
        return x


# Initializing the model
m = Model()

