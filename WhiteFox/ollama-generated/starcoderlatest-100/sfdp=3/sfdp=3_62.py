
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, qk, key, v):
        dropout_qk = torch.nn.functional.dropout(qk, p=dropout_p)
        output = dropout_qk.matmul(v)
        return output


# Inputs to the model
query = torch.randn(2, 8, 64, 64)
key   = torch.randn(2, 8, 64, 64)
value = torch.randn(2, 8, 64, 64)
