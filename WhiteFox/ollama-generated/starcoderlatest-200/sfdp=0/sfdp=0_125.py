
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention()
 
    def forward(self, query, key, value, scale=1):
        attention_weights  = self.attention(query, key, value, padding_mask) 
        scaled_dot_product = torch.matmul(attention_weights, value) / scale
        output             = torch.matmul(scaled_dot_product, attention_weights.transpose(-2, -1))
        return output


# Initializing the model
m = Model()

# Inputs to the model
query  = torch.randn(32, 64, 7, 10)
key    = torch.randn(8, 64, 7, 10)
value  = torch.randn(32, 64, 7, 10)
