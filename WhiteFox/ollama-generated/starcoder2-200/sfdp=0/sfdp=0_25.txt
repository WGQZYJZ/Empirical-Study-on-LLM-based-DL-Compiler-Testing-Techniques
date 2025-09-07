

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        inv_scale  = torch.sqrt(x1)
        scaled_dot_product  = torch.matmul(x1, query.transpose(-2, -1)) / inv_scale
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        output  = attention_weights.matmul(value)
        return output

# Initializing the model
m = Model()

 # Inputs to the model
query  = torch.randn(64, 32, 64)
key  = torch.randn(64, 800, 160)
value  = torch.randn(64, 800, 512)
 
x1  = torch.matmul(query, key.transpose(-2, -1)) / x3 # The scaling factor is the third input tensor. We need to multiply it with the first two inputs.

__output__  = m(x1)

