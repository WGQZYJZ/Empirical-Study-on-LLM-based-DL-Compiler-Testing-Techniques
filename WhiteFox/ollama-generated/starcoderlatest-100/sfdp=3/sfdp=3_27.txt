
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(8, 32)
 
    def forward(self, q, k, v):
        scaled_qk = torch.matmul(q, k.transpose(-2, -1)) * scale_factor
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = self.attention(x=softmax_qk, key_padding_mask=None)[0]
        output = torch.nn.functional.dropout(dropout_qk, p=dropout_p)
        return output


# Inputs to the model
q  = torch.randn(1, 32, 768, 8)
k  = torch.randn(1, 32, 768, 8)
v  = torch.randn(1, 32, 512, 8)
