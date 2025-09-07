

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.Dropout(p=0.2)
        self.scale  = torch.tensor([5, ])
 
    def forward(self, query, key):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk / self.scale[None]
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk  = self.dropout(softmax_qk)
        output  = dropout_qk.matmul(value)

        return v6

m2  = Model()
xq, xk, xv  = torch.randn(3, 4), torch.randn(3, 4), torch.randn(5, 3)
__output__  = m(x1)

