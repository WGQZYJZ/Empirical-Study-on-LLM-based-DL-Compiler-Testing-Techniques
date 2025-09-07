
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, query, key, value):
        scaled_dot_product  = torch.matmul(query, key.transpose(-2, -1)) / inv_scale
        attention_weights   = scaled_dot_product.softmax(dim=-1)

        output               = attention_weights.matmul(value)
        return output

class Model(torch.nn.Module):
    def __init__(self):
         super().__init__()

    def forward(self, x1, x2):
         m1  = Attention()
         v1  = m1(x1, x1, x2)

         m2  = Attention()
         v2  = m2(x2, x1, x1)
   
         return torch.cat((v1, v2), dim=1)

m = Model()
x1 = torch.randn(32, 50)
x2 = torch.randn(32, 768)
__output__  = m(x1, x2)

