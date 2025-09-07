
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 5)
 
    def forward(self, qk):
        scaled_qk = qk / scale_factor
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = F.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(v)
        return self.linear(output), None


# Initializing the model
m = Model()

# Query
qk = torch.randn(1, 5, 32)
__output__, __attention__ = m(qk)


