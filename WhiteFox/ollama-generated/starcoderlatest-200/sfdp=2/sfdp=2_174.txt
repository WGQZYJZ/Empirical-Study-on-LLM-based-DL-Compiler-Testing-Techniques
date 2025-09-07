
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(2, 16)
 
    def forward(self, q1, k1, v1):
        scaled_qk, attn_weights = self.attn(q1, k1, v1)
        scaled_qk = scaled_qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        output = dropout_qk.matmul(value)
