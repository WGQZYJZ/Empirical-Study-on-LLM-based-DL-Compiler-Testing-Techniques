
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        scaled_dot_product  = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(key.shape[-1]) 
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        output  = attention_weights.matmul(value)
        return output

m = Model()
query  = torch.randn(4, 5, 768)
key  = torch.randn(4, 5, 768)
value  = torch.randn(4, 1024, 768)

__output__  = m(query, key, value)

