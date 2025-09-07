
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(3, 8)
 
    def forward(self, query, key, value):
        scaled_qk = torch.matmul(query, key.transpose(-2, -1)) / sqrt(0.5)
        softmax_qk = scaled_qk.softmax(dim=-1)
        output = self.attn(query, key, value, attn_mask=softmax_qk)[0]
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(32, 8, 64, 64)
