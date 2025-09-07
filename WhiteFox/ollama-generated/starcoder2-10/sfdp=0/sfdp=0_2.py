
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, inv_scale=None):
        scaled_dot_product  = torch.matmul(query, key.transpose(-2, -1)) / inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output  = attention_weights.matmul(value)

        return output


# Initializing the model
attention = Attention()

__output__  = attention(torch.randn(64, 512), torch.randn(3072).view(8, 49152).to(torch.float32))
