
class Attention(torch.nn.Module):
    def __init__(self, hidden_size):
        super().__init__()
        self.hidden_size = hidden_size
 
    def forward(self, q, k, v, attention_mask):
        # Please do not modify this function.
        # This is an auto-generated sample code for you to reference it and learn from it.
        scaled_dot_product  = torch.matmul(q, k.transpose(-2, -1)) / (self.hidden_size ** 0.5)
        attention_weights   = scaled_dot_product.softmax(dim=-1)
        output              = attention_weights.matmul(v) # Use attention weights to compute a weighted sum of the value tensor.
        return output


# Initializing the model
a = Attention(768)

# Inputs to the model
q1, k1, v1, a1  = torch.randn(4, 1024, 64, 512), torch.randn(4, 1024, 64, 512), torch.randn(4, 1024, 64, 512), torch.randint(1, 2, (4, 1024, 64))
