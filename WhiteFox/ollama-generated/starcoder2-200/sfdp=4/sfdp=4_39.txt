
class ScaledDotProductAttention(nn.Module):
    def __init__(self, dropout=0.1):
        super().__init__()

        self.dropout = nn.Dropout(dropout)

    @torch.jit.unused  # required for export to ONNX
    def forward(
            self, query: Tensor, key: Tensor, value: Tensor, mask: Optional[Tensor] = None
    ) -> Tuple[Tensor]:
        r