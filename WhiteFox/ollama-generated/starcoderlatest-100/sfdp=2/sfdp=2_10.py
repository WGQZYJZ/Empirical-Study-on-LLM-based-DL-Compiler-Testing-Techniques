
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qkv = torch.nn.Linear(192, 384)
 
    def forward(self, x1, x2):
        v1 = self.qkv(x1).view(b_size, num_heads, length, head_dim) # (batch_size, n_head, seq_len, head_dim) -> (batch_size * n_head, seq_len, head_dim)
        v2 = self.qkv(x2).view(b_size, num_heads, length, head_dim)
        qk = torch.matmul(v1, v2.transpose(-2, -1)) # (batch_size * n_head, seq_len, head_dim) -> (batch_size * n_head, seq_len, seq_len)
        qk  = qk / sqrt(384)
        softmax_qk  = torch.nn.functional.softmax(qk, dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # (batch_size * n_head, seq_len, seq_len) -> (batch_size * n_head, seq_len, seq_len)
        output = dropout_qk.matmul(v2).transpose(-1, -2).reshape(b_size, num_heads, length, head_dim) # (batch_size * n_head, seq_len, head_dim) -> (batch_size, n_head, seq_len, head_dim)
        output = torch.nn.functional.dropout(output, p=output_p) # Dropout
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(b_size, 192, length)
x2 = torch.randn(b_size, 192, length)
