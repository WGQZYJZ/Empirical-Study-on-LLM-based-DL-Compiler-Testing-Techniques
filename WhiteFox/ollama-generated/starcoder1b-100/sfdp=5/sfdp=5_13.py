
class Model(torch.nn.Module):
    def __init__(self, embed_dim=2048, hidden_dim=1024, num_heads=8, num_layers=2):
        super().__init__()
        self.embed = torch.nn.Embedding(vocab_size, embed_dim)
        self.transformer = Transformer(
            dim=embed_dim, hidden_dim=hidden_dim, num_heads=num_heads, num_layers=num_layers
        )
 
    def forward(self, x):
        x = self.embed(x)  # Embedding layer on the input
        x = self.transformer(x)  # Apply transformer to the input
        return x


# Initializing the model
m = Model()


