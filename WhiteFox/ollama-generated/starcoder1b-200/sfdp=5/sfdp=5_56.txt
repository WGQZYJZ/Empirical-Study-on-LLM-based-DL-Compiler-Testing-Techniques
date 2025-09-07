
class Model(torch.nn.Module):
    def __init__(self, n_layers=2, d_key=100, d_model=512, nhead=8):
        super().__init__()
        self.n_layers = n_layers
        self.d_key = d_key
        self.d_model = d_model
        self.nhead = nhead
        # Embedding layer
        self.embedding = torch.nn.Embedding(self.vocab_size, self.d_model)

        # Encoder layers
        for _ in range(self.n_layers):
            layer = TransformerEncoderLayer(self.d_key, self.d_model, nhead=self.nhead)
            setattr(self, f"layer{_}", layer)

        # Decoder layers
        for _ in range(self.n_layers - 1):
            layer = TransformerDecoderLayer(self.d_key, self.d_model, nhead=self.nhead)
            setattr(self, f"layer{_ + 1}", layer)

    def forward(self, x):
        # Embed the inputs
        x = self.embedding(x).float()

        # Forward through layers
        for layer in range(self.n_layers):
            x = getattr(self, f"layer{layer}")(x)

        # Return the output
        return x

# Initializing the model
m = Model()

# Inputs to the model
inputs = torch.randn(2, 3, 64, 64)
