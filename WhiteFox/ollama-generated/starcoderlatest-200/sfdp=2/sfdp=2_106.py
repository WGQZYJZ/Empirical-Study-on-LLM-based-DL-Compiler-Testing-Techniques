
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, qk, vq, kv):
        return self.attention(x1, qk, vq, kv)

    # Attention pattern
    def attention(qk, qkv, xv, dropout_p=0.2):
        scaled_qk = qk * inv_scale_factor
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(vq)  # compute the dot product of the dropout output and the value
