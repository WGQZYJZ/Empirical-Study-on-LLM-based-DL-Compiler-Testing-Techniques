
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(4, 8)
 
    def forward(self, qk_in):
        v1 = torch.matmul(qk_in[0], qk_in[1].transpose(-2, -1)) / 512
        v2 = v1 + self.linear(v1) * 0.7071067811865476
        v3 = torch.nn.functional.dropout(torch.softmax(v2), p=dropout_p, training=training)
        output = v3.matmul(qk_in[1]) + qk_in[0]
        return output

# Inputs to the model
qk_in  = (torch.randn(batchsize, dim, nhead, head_dim), torch.randn(batchsize, dim, nhead, head_dim))
