
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.Linear(d_model, d_model)
        self.dropout = nn.Dropout(0.1)

    def forward(self, x1, x2, mask=None):
        qk = torch.matmul(x1, x2.transpose(-2, -1)) / math.sqrt(x1.size(-1))

        if mask is not None:
            attn_mask = mask * 0.1  # [batch_size, length, seq_len]
        else:
            attn_mask = None  # [batch_size, length, seq_len]

        # Compute the weighted sum of `value` and `key` with a scaled dot-product attention mechanism.
        attn_weight = torch.softmax(qk, dim=-1) * x2
        if self.training:
            return attn_weight  # Return an input tensor to be used in an optimization process, i.e., loss calculation
        else:
            value = torch.matmul(attn_weight, x1)
            output = value + x1
            return output


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
