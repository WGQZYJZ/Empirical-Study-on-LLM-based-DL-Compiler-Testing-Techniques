
class TransformerModel(torch.nn.Module):
    def __init__(self, d_model=512, nhead=8):
        super().__init__()
        self.encoder = torch.nn.TransformerEncoderLayer(d_model=d_model, nhead=nhead)
 
    def forward(self, src: Tensor, attn_mask: Optional[Tensor] = None) -> Tuple[Tensor]:
        output  = self.encoder(src, attn_mask).transpose(-2, -1)  # Shape: (bsz * tgt_len, tgt_len, d_model)
        return torch.softmax(output, dim=-1), torch.log(torch.mean(torch.softmax(output, dim=-1)))
