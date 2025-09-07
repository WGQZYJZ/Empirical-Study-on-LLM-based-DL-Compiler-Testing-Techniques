
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = torch.nn.Parameter(1)
 
    def forward(self, query, key, value):
        scaled_dot_product  = torch.matmul(query, key.transpose(-2, -1)) / inv_scale
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        output  = attention_weights.matmul(value)
        return output


m  = Model()
qry  = torch.randn(8, 300)
key = torch.randn(8, 300)
val  = torch.randn(8, 2048)
__output__  = m(qry, key, val)

