
class TransformerEncoderLayer(torch.nn.Module):
    def __init__(self, d_model: int = 512, nhead: int = 8, dim_feedforward: int = 2048, dropout: float = 0.1):
        super().__init__()

        self._layernorm1 = torch.nn.LayerNorm(d_model)
        self._conv = torch.nn.Conv1d(in_channels=d_model + nhead * d_model // 2, out_channels=dim_feedforward, kernel_size=9)

    def forward(self, x):
        