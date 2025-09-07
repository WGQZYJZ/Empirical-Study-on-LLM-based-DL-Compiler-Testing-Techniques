
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, q1, k1, v1):
        scaled = torch.matmul(q1, k1.transpose(-2, -1)) / 3072.0
        softmax_qk = scaled.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.1)
        output = dropout_qk.matmul(v1)

# Initializing the model
m  = Model()

# Inputs to the model
q1  = torch.randn(8, 64, 32, 57)
k1  = torch.randn(8, 64, 32, 57)
v1  = torch.randn(8, 64, 32, 57)


__output__  = m(q1, k1, v1)
