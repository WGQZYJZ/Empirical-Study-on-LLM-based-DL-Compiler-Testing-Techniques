
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, inv_scale=None):
        scaled_dot_product  = torch.matmul(query, key.transpose(-2,-1)) / (inv_scale if inv_scale else math.sqrt(key.size(-1)))
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(value)
        return output


# Initializing the model 
m = Model()
__output__  = m(torch.randn(2, 5), torch.randn(2, 64, 3072), torch.randn(2, 1088))

Input: torch.Size([2, 5]) torch.Size([2, 64, 3072]) torch.Size([2, 1088])
Output: torch.Size([2, 1088])

