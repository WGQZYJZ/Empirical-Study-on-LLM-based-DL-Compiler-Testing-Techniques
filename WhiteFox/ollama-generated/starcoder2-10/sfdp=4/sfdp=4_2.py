
class TransformerBlock(nn.Module):
    def __init__(self, embed_dim: int, dropout: float = 0., bias: bool = False) -> None:
        super().__init__()
        self.layernorm1 = nn.LayerNorm(embed_dim, eps=1e-6)
        self.dropout1 = nn.Dropout(p=dropout)
        self.linear1 = nn.Linear(in_features=embed_dim, out_features=embed_dim // 2, bias=bias)
 
        self.layernorm2 = nn.LayerNorm(embed_dim, eps=1e-6)
        self.dropout2 = nn.Dropout(p=dropout)
        self.linear2 = nn.Linear(in_features=embed_dim // 2, out_features=embed_dim, bias=bias)
 
        self.linear3 = nn.Linear(in_features=embed_dim * 4, out_features=embed_dim)
 
    def forward(self, hidden: torch.Tensor) -> torch.Tensor:
        residual = hidden

        hidden1 = self.layernorm1(hidden) + self.dropout1(self.linear1(hidden))
        hidden2 = self.layernorm2(hidden1) + self.dropout2(self.linear2(hidden1))
 
        hidden3 = torch.cat([residual, hidden2], dim=1)  # Join hidden and hidden_r with axis = 1
        return self.linear3(hidden3)
class Transformer(nn.Module):
    def __init__(self) -> None:
        super().__init__()

        self._model = nn.Sequential(*[TransformerBlock(2048, bias=True),
                                      TransformerBlock(2048)])

    def forward(self, hidden: torch.Tensor) -> torch.Tensor:
        return self._model(hidden).sum(dim=-1)


# Initializing the model
t = Transformer()
 
# Inputs to the model
x  = torch.randn(65, 4096)
 
__output__  = t(x)