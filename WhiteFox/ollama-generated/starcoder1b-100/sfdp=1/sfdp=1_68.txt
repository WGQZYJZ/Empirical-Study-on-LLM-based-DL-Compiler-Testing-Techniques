
class Model(torch.nn.Module):
    def __init__(self, embed_dim=128):
        super().__init__()
        self.embedding = torch.nn.EmbeddingBag(vocab_size, embed_dim)
        # We use the same linear layer as in the Transformer model for simplicity

    def forward(self, input_ids):
        _, hidden_states = self.embedding(input_ids)
        hidden_states  # The output of the embedding function
        # ...


# Initializing the model
m  = Model()

