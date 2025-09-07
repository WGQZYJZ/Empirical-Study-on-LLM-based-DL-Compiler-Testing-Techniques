
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, attention_dropout=0., dropout=0.):
        super().__init__()
        self.attention_dropout = torch.nn.Dropout(attention_dropout)
        self.dropout = torch.nn.Dropout(dropout)
 
    def forward(self, qk: torch.Tensor, v: torch.Tensor, attn_mask: Optional[torch.Tensor] = None):
        # (bsz, nheads, lenq, lenkv), (bsz, nheads, lenv, d_head), mask
        attention_weights  = torch.matmul(qk, k.transpose(-2, -1)) / inv_scale
        # Compute softmax on each row and take the exponential value. This will create a distribution over all heads, with the most important head being weighted more than the rest of them by `attn_dropout`
        attention_weights = self.attention_dropout(F.softmax(attention_weights, dim=-1))

        # (bsz, nheads, lenq, d_head) * (bsz, nheads, lenv, d_head) -> (bsz, nheads, lenq, d_head), then take a weighted sum
        # (attn_mask is optional and has shape (bsz, lenq, lenk))
        context = torch.matmul(attention_weights, v).transpose(-2, -1)

        # Apply dropout
        context = self.dropout(context)
        
        return context


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = ScaledDotProductAttention()
 
    def forward(self, qk: torch.Tensor, v: torch.Tensor, attn_mask: Optional[torch.Tensor] = None):
        context = self.attn(qk, v)

        # (bsz, lenq, d_head), (bsz, lenv, d_head), mask
        output = torch.matmul(context, k)
        
        return output
