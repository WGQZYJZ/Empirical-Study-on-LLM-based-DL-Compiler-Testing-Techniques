
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(2, 8)
 
    def forward(self, q, k, v, input_tensor):
        scaled_qk = self.attn(q, k, v)[0]
        softmax_qk = scaled_qk.softmax(-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(v)
        return output


# Initializing the model
m = Model()


# Inputs to the model
query = torch.randn(1, 3, 64, 64)
key   = torch.randn(2, 8, 64, 64)
value = torch.randn(2, 8, 64, 64)
input_tensor = torch.randn(1, 8, 32, 32)
