
class Model(torch.nn.Module):
    def __init__(self, d_k, d_v, nhead):
        super().__init__()
        self.scale = math.sqrt(d_k)
        self.proj = torch.nn.Linear(d_v, d_k)
        self.query = torch.nn.Linear(nhead * d_v, d_k)
        self.key = torch.nn.Linear(nhead * d_v, d_k)
        self.value = torch.nn.Linear(nhead * d_v, d_v)

    def forward(self, x1, x2):
        # shape (batch, query_seq_len, input_dim) -> batch, query_seq_len, nhead, input_dim / nhead, output_dim
        query = self.query(x1).view(-1, 1, 1, x1.shape[-2] // 1).expand(
            -1, x2.shape[0], self.scale)

        # shape (batch, key_seq_len, input_dim) -> batch, key_seq_len, nhead, input_dim / nhead, output_dim
        key = self.key(x2).view(-1, 1, 1, x2.shape[-2] // 1).expand(
            -1, x1.shape[0], self.scale)

        # shape (batch, key_seq_len, input_dim) -> batch, query_seq_len, nhead, input_dim / nhead, output_dim
        value = self.value(x2).view(-1, 1, x2.shape[-2] // 1).expand(
            -1, x1.shape[0], self.scale)

        # shape (batch, query_seq_len, output_dim) -> batch, nhead, input_dim / nhead, output_dim
        attention = torch.matmul(query, key.transpose(-2, -1)) / self.scale

        # shape (batch, nhead, input_dim / nhead, output_dim) -> batch, query_seq_len, nhead, input_dim / nhead, output_dim
        attention = attention.view(-1, self.scale, self.scale, x2.shape[-2] // 1, -1).permute(
            0, 3, 4, 2, 1)

        # shape (batch, nhead, input_dim / nhead, output_dim) -> batch, nhead, query_seq_len, input_dim / nhead
        attention = attention.contiguous().view(-1, self.scale * self.scale, -1)

        # shape (batch, nhead, query_seq_len, input_dim / nhead) -> batch, nhead, query_seq_len, output_dim
        output = torch.matmul(attention, value).contiguous().view(
            -1, self.scale, x2.shape[0], x1.shape[-2] // 1, self.scale * self.scale).permute(
            0, 3, 4, 1)

        # shape (batch, nhead, query_seq_len, output_dim) -> batch, nhead, query_seq_len, input_dim / nhead
        return output


# Initializing the model
m = Model(d_k=8, d_v=8, nhead=2)


