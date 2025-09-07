
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(8, 3)
 
    def forward(self, query, key, value):
        qk = self.attn(query, key, value)[0]
        scaled_qk = qk / (1.0 / scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 8, 64, 64)
