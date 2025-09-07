
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, num_head, d_k, d_v):
        super().__init__()
        self.num_head = num_head
        self.d_k = d_k
        self.d_v = d_v

        # Weights for the query/key and value linear projections. They are different to `mha`.
        # It is different from the original paper in that we have splited key/value weights into different heads
        self.query = torch.nn.Linear(in_features=d_model, out_features=num_head * d_k)
        self.key = torch.nn.Linear(in_features=d_model, out_features=num_head * d_k)

    # The output of the linear projections are then multiplied by scale factor to generate a QK tensor
    def forward(self, query, key):
        batch_size = query.shape[0]
        qkv = torch.cat((query, key), dim=1).view(batch_size, -1, self.num_head * self.d_k)  # [B*N, num_heads * d_k]
        qk = self.query(qkv).view(-1, batch_size, self.num_head, self.d_k)  # [B, N, num_heads, d_k]
        kv = self.key(qkv).view(-1, batch_size, self.num_head, self.d_k)  # [B, N, num_heads, d_k]

        # The dot product of a query and a key is computed in this section. We are using scaled dot products here,
        # where the scaling is done after the elementwise multiplication of two inputs instead of before them
        qkv = qk * inv_scale_factor + kv * scale_factor  # [B*N, num_heads, d_k]

        # Softmax will be applied on the last axis to generate a softmax tensor which is multiplied by the dropout probability p
        softmax_qk = softmax(qkv)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # [B*N, num_heads, d_k]

        output = torch.matmul(dropout_qk, kv).view(-1, batch_size, self.num_head * self.d_v)
        return output
# Initializing the model
m = MultiHeadAttention(1024, 36, 768)


# Inputs to the model
x1 = torch.randn(1, d_model=512, seq_len=1024)
x2 = torch.randn(1, d_model=512, seq_len=1024)
