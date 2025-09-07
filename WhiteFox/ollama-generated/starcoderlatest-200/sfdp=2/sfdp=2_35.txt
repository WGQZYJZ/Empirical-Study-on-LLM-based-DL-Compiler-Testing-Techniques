
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(embed_dim=256, num_heads=4)
 
    def forward(self, q1, k1, v1):
        scaled_qk, softmax_qk, dropout_qk =  # (1) Compute the dot product of query with keys, softmax and dropout them.
            self.attention(q1, k1, v1)  # (2) Pass through attention layer to compute qk, key, value
        output = dropout_qk.matmul(v1)  # (3) Compute the dot product of the dropout output and value
        return output
