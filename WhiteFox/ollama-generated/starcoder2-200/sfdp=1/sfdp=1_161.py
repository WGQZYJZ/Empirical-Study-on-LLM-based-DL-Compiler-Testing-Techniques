
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.att = torch.nn.MultiheadAttention(2, 10)
 
    def forward(self, q1, k1, v1, dropout_p=0.5):
        scaled_qk = self.att(q1, k1)[0] / (64 ** 0.5)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk @ v1 
        return output


# Initializing the model with input tensor 32x4x8 and output tensor 56x4x4
m = Model()
q1 = torch.randn(32, 4096).chunk(7)[-1] # A single query matrix in the first head of MultiheadAttention
k1 = torch.randn(32, 4096)            # An arbitrary key tensor used as the input to the model
v1 = torch.randn(56, 8, 8)             # A value vector in the first head of MultiheadAttention
 

x1 = m(q1, k1, v1, dropout_p=0.5)

