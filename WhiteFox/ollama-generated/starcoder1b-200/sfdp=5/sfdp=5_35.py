
class Model(torch.nn.Module):
    def __init__(self, num_heads=8):
        super().__init__()
        self.embedding = torch.nn.Embedding(vocab_size, hidden_dim)
        self.encoder = torch.nn.TransformerEncoder(
            # ...
        )
 
    def forward(self, x1, x2, attn_mask):  # __output__
        