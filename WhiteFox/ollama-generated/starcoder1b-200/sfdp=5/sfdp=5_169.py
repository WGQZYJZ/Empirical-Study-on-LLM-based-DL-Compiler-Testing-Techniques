
class Model(torch.nn.Module):
    def __init__(self, attn_layers=2, heads=1, dim_feedforward=32):
        super().__init__()
        self.attn = Attention()
        self.ffn = torch.nn.Sequential(
            torch.nn.Linear(dim_feedforward, 4 * dim_feedforward),
            torch.nn.ReLU(),
            torch.nn.Linear(4 * dim_feedforward, heads * dim_feedforward),
            torch.nn.Softmax()
        )
        self.layer_norm1 = torch.nn.LayerNorm(dim_feedforward)

    def forward(self, x1):
        return self.attn(x1, x1)

    @property
    def attention(self):
        return self.attn
