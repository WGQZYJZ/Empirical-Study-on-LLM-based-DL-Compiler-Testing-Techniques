
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.multihead_attention = torch.nn.MultiheadAttention(3, 8)
 
    def forward(self, x1):
        scaled_dot_product = torch.matmul(x1, key.transpose(-2, -1)) / inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(value)
        return output


# Inputs to the model
q = torch.randn(2048, 3, 64, 64)
k = torch.randn(16, 3, 64, 64)
v = torch.randn(16, 3, 64, 64)
inv_scale = math.sqrt(0.5) # The inverse scale factor is set to 1/8 by default. Please note that this may need to be adjusted for different datasets and applications.
