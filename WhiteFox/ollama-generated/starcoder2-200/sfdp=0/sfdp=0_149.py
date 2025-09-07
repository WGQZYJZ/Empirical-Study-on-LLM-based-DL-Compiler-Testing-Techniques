

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.scale = 1 / math.sqrt(d)
 
    def forward(self, input_, query, key):
        scaled_dot_product  = torch.matmul(query, key.transpose(-2,-1)) * self.scale
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        output  = attention_weights.matmul(value)
        return output

# Initializing the model:
m  = Model()

 # Inputs to the model
input_  = torch.randn(32, 56, 7, 80)
query  = torch.randn(143, d)
key   = torch.randn(d, 34)
__output__  = m(input_, query, key)

