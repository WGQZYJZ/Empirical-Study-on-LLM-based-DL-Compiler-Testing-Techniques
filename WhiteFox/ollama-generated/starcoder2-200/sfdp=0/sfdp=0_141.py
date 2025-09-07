
class Transformer(torch.nn.Module):
    def __init__(self, input_dim=768, n_heads=12, dropout=0.5, activation="gelu"):
        super().__init__()

        self.encoder = torch.nn.TransformerEncoderLayer(d_model=input_dim, nhead=n_heads)
        self.dropout = torch.nn.Dropout(p=dropout)
 
    def forward(self, x1):
        v2  = self.encoder(x1)
        v3  = self.dropout(v2)
        return v3


# Initializing the model
m  = Transformer()

# Inputs to the model
x1 = torch.randn(8, 64, 768)

