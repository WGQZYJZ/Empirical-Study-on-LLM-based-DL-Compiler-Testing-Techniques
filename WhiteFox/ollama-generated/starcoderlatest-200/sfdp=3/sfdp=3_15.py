
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(128, 32)
 
    def forward(self, x1, x2, x3):
        qk, v_attn = self.attention(x1, x2, x3) # Use attention module to compute dot products of query and key with corresponding multi-head
        scaled_qk = torch.matmul(qk, key.transpose(-2, -1)) * scale_factor
        softmax_qk = scaled_qk.softmax(dim=-1) 
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = torch.matmul(dropout_qk, value)
        return output

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 128, 4096, 32)
x2 = torch.randn(1, 128, 4096, 64)
x3 = torch.randn(1, 128, 32, 64)


