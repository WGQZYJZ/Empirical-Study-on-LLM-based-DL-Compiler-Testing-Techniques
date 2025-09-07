
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(128, 128)
 
    def forward(self, x, y, query_len, key_len, scale_factor):
        qk = self._matmul(x, y, query_len, key_len)
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = torch.nn.functional.softmax(scaled_qk, dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.5)
        output = dropout_qk.matmul(y)
        return output
 
    def _matmul(self, x, y, query_len, key_len):
        # Do matrix multiplication between the inputs `x` and `y`, and
        # transpose the result such that it can be directly passed to softmax
        qk = torch.einsum('bhik,bhij->bhil', (x, self.query(y).unsqueeze(-1))).transpose(0, 2)
        return qk
# Initializing the model
m = Model()
 
# Inputs to the model
x = torch.randn(4, 16, 100, 75)
y = torch.randn(4, 16, 100, 75)
query_len = [2, 3]
key_len = [2, 2]
scale_factor = 1 / torch.sqrt(torch.tensor(9))
 
