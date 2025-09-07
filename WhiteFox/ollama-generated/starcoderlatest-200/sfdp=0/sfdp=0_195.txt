
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(num_heads=8)
 
    def forward(self, q1, k1, v1):
        attention_weights  = self.attention(q1, k1, value=v1)[0] # The output of Multihead Attention is a tuple containing the output tensor, attention weights and optional context vectors. Here we only need the output tensor.
        scaled_dot_product = torch.matmul(q1, k1.transpose(-2, -1)) / math.sqrt(k1.shape[-1]) # The scaled dot product matrix is defined in multi-head attention function. We do not need to compute it again because there are already computed.
        output = scaled_dot_product.matmul(v1)
        return output


# Initializing the model
m = Model()

# Inputs to the model
q1 = torch.randn(8, 64, 256, 256) # The number of heads is set to 8 for this example.
k1 = torch.randn(8, 64, 256, 256)
v1 = torch.randn(8, 64, 256, 256)
