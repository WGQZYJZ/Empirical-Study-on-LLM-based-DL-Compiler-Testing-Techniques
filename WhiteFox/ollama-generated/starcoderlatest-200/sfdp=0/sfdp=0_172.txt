
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, value, inv_scale):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(value)
        return output

# Input to the model
query  = torch.randn(2, 3, 64, 64)
key    = torch.randn(3, 8,  64, 64)
inv_scale = math.sqrt(64 * 64 / (2 * 3)) # The scale factor is set to sqrt of the dimensions of key/query vectors
