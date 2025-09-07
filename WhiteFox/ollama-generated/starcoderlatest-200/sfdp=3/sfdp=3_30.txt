
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(embed_dim=16, num_heads=4)
 
    def forward(self, query, key, value):
        qk  = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output


# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(8, 16, 32, 10) # (batch_size, embedding_dim, query_length, dkv_length)
key = torch.randn(4, 16, 32, 9)
value = torch.randn(8, 16, 64, 8)
