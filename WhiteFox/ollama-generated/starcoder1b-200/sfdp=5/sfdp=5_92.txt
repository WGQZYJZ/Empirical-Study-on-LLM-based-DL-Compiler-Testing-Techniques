
class Model(torch.nn.Module):
    def __init__(self, embed_dim, depth, num_heads, qkv_bias=True, dropout_p=0.1, attn_dropout_p=0.1):
        super().__init__()
 
        # Embedding layer
        self.embed_layer = torch.nn.Embedding(vocab_size, embed_dim)

        # Transformer layers and feedforward
        layers = [
            torch.nn.Linear(embed_dim, embed_dim),
            torch.nn.ReLU(),
            torch.nn.Linear(embed_dim, embed_dim * 2),
            torch.nn.ReLU(),
            torch.nn.Linear(embed_dim * 2, embed_dim * 2),
            torch.nn.ReLU(),
        ]

        self.layers = torch.nn.ModuleList()
        for _ in range(depth):
            layers += [
                TransformerLayer(embed_dim * 2),
                torch.nn.ReLU(),
            ]
 
        self.transformer = nn.Sequential(*layers)

        # Linear layer and activation function (no bias)
        self.linear_layer = torch.nn.Linear(embed_dim * 2, vocab_size)
        self.linear_act_layer = torch.nn.ReLU()

    def forward(self, x):
        x = self.embed_layer(x)
        x = self.transformer(x)
        x = self.linear_act_layer(self.linear_layer(x))
        return F.softmax(x, dim=-1), x


# Inputs to the model
x  = torch.randn(16, 4)
__output__, _  = m(x)
