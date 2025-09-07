
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Parameter(torch.randn(1, 5, 7, 7))
        self.key   = torch.nn.Parameter(torch.randn(1, 5, 6, 7))
        self.value = torch.nn.Parameter(torch.randn(1, 3, 64, 64))
 
    def forward(self, x1):
        qk = torch.matmul(x1, self.query)
        scaled_qk = qk.div(torch.sqrt(torch.sum(self.key ** 2, dim=-1, keepdim=True)))
        softmax_qk = scaled_qk.softmax(-2)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        out   = dropout_qk.matmul(x1, self.value)
        return out

# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 5, 7, 7)
y1  = m(x1)
z2  = m(torch.ones_like(y1))
