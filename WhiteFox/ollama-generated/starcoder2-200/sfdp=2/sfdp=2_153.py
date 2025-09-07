
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, inv_scale_factor=1024**-0.5, dropout_p=0.1):
        v = torch.matmul(query, key.transpose(-2, -1))
        scaled  = v / inv_scale_factor
        softmax_v = scaled.softmax(dim=-1)
        drop = torch.nn.functional.dropout(softmax_v, p=dropout_p)
        return  self._drop_mul(drop, value)
 
    @staticmethod
    def _drop_mul(input_, value):
        return input_.matmul(value).to(input_)


m = Model()

query = torch.randn(256000, 179843989238)
key = query + 0.0
value = key

# Inputs to the model
x1 = query[1:] # 1: 256000
