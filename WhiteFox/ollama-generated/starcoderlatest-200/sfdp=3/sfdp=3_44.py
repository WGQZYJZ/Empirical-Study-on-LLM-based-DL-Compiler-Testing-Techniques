
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention()
 
    def forward(self, query, key, value):
        v1 = qk = torch.matmul(query, key.transpose(-2, -1)) * scale_factor
        v2 = scaled_qk = v1.mul(scale_factor)
        v3 = softmax_qk = v2.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(v3, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output


# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(8, 64, 1024, 1024)
key   = torch.randn(8, 1024, 512, 512)
value = torch.randn(8, 512, 3, 3)
