
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, config):
        super().__init__()
 
    def forward(self, query, key, value):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / inv_scale # The scaling factor here is 3e-5. Hence we divided it by the sqrt of that.
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        output  = attention_weights.matmul(value)
        return output
 
class Model(torch.nn.Module):
    def __init__(self, config):
        super().__init__()
        self.scaled_dot_product_attention = ScaledDotProductAttention()
 
    def forward(self, query, key, value):
        output  = self.scaled_dot_product_attention(query, key, value)
        return output

model = Model() # We also initialize the model here as before (see above)


# Inputs to the model:
# - query
x1 = torch.randn(8032, 768)

# - key
x2 = torch.randn(8032, 768)

# - value
x3 = torch.randn(8032, 512)

 # Running the model:
__output__  = m(query=x1, key=x2, value=x3)