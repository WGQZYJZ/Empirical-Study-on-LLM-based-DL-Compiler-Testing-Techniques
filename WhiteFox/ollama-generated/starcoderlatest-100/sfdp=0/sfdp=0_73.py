
class Model(torch.nn.Module):
    def __init__(self, inv_scale: float = 16.0):
        super().__init__()
        self.inv_scale = inv_scale
 
    def forward(self, query, key, value):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / self.inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(value)
        return output

# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(4, 8, 64, 64) # The query can be any tensor with shape (batch_size, head_num * hidden_dim). It will be used as a context vector and projected on `head_num` different heads at first. Then the heads are multiplied by a constant `scale`, which is usually defined to be 1/sqrt(attention_heads).
key = torch.randn(4, 8, 64, 64) # The key can also be any tensor with shape (batch_size, head_num * hidden_dim). It will be used as a context vector and projected on `head_num` different heads at first. Then the heads are multiplied by a constant `scale`, which is usually defined to be 1/sqrt(attention_heads).
value = torch.randn(4, 8, 64, 64) # The value can also be any tensor with shape (batch_size, head_num * hidden_dim). It will be used as a context vector and projected on `head_num` different heads at first. Then the heads are multiplied by a constant `scale`, which is usually defined to be 1/sqrt(attention_heads).
