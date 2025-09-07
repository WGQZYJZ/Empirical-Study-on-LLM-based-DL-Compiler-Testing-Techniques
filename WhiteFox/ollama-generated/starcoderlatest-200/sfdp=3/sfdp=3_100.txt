
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention()
 
    def forward(self, query, key, value):
        scaled_qk = self.attention(query, key, key)
        softmax_qk = scaled_qk.softmax(dim=-1)
        output = self.attention(output=value, attention_mask=softmax_qk).matmul(scale_factor)
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(32, 16, 1024, 1024)
x2 = torch.randn(128, 32, 512, 512)
