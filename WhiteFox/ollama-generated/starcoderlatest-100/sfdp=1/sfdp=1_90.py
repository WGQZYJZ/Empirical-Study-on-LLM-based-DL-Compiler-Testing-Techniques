
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(8, 16)
 
    def forward(self, query, key, value):
        qk = self.attention(query, key, value)[0]
        softmax_qk = self.softmax(qk).div(self.scale_factor)
        output = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        return self.matmul(output, value)
 
    def matmul(self, qk, value):
        return torch.matmul(qk, value.transpose(-2, -1))


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
query = torch.randn(16, 8, 64, 64)
key   = torch.randn(16, 8, 64, 64)
value = torch.randn(16, 8, 64, 64)
