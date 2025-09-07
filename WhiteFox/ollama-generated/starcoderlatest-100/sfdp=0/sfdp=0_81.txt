
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention()
 
    def forward(self, q, k, v):
        scaled_dot_product = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(k.shape[-1])
        attention_weights = torch.softmax(scaled_dot_product, dim=-1)
        output = torch.matmul(attention_weights, v)
        return output


# Initializing the model
m = Model()

# Inputs to the model
q = torch.randn(256, 32, 4096, 768) # The first dimension is batch size
k = torch.randn(256, 64, 4096, 768)
v = torch.randn(256, 128, 4096, 768)
