
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, qk_scale=None, attn_dropout=0.1):
        super().__init__()
        self.wq = torch.nn.Linear(d_model, d_model)  # query: batch_size * nhead * seq_len * hidden_dim, key: batch_size * nhead * seq_len * hidden_dim
        self.wk = torch.nn.Linear(d_model, d_model)  # key: batch_size * nhead * seq_len * hidden_dim, value: batch_size * nhead * seq_len * hidden_dim

        if qk_scale is not None:
            inv_sqrt = 1 / (qk_scale ** 0.5)
        else:
            inv_sqrt = 1 / torch.sqrt(torch.tensor(d_model))

        self.scale = qk_scale * inv_sqrt
        self.dropout = torch.nn.Dropout(attn_dropout)

    def forward(self, x, key, value, mask=None):
        if mask is not None:
            m = x.unsqueeze(2).unsqueeze(1)  # x: batch_size * nhead * seq_len * input_dim
            m = self.dropout(torch.sigmoid(self.wq(m) * self.wk(key)))
            m = m * mask
        else:
            m = x.unsqueeze(2).unsqueeze(1)  # x: batch_size * nhead * seq_len * input_dim
            m = self.dropout(torch.sigmoid(self.wq(m) * self.wk(key)))

        m = m.transpose(1, 2)  # m: batch_size * seq_len * nhead * input_dim
        return torch.matmul(m, value), m


# Initializing the model
m = ScaledDotProductAttention()


