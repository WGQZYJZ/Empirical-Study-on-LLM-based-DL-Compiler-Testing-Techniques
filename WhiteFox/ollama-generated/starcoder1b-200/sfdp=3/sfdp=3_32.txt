
class Model(torch.nn.Module):
    def __init__(self, embedding_dim, hidden_dim, num_layers=2, layer_norm=True):
        super().__init__()

        self.embedding = torch.nn.Embedding(vocab_size, embedding_dim)
        self.transformer = Transformer(
            d_model=embedding_dim,
            nhead=4,
            dim_feedforward=hidden_dim // 2,
            num_layers=num_layers,
            layer_norm=layer_norm,
        )

    def forward(self, x):
        x = self.embedding(x)

        x = self.transformer(x)

        return x


# Initializing the model
model = Model()


