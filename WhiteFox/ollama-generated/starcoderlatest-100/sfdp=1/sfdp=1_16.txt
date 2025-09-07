
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(8, 16)

    def forward(self, query, key, value):
        scaled_qk = self.attn(query, key, key)[0] * inv_scale_factor
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output


# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(1, 32, 512) # (bsz x nHeads x qLen x kDim), for instance bsz = 4, qLen = 64, kDim = 64
key   = torch.randn(1, 1024, 8) # (bsz x nHeads x kLen x vDim), for instance bsz = 32, kLen = 512, vDim = 8
value = torch.randn(1, 16, 64, 128) # (bsz x nHeads x qLen x vDim), for instance bsz = 4, qLen = 64, vDim = 128
