
class Model(torch.nn.Module):
    def __init__(self, query_dim=16, key_dim=16, inv_scale=8, heads=4):
        super().__init__()
        self.query_dim  = query_dim
        self.key_dim    = key_dim
        self.inv_scale  = inv_scale
        self.heads      = heads
 
    def forward(self, x1, x2):
        x1_expand     = torch.cat((x1, x1), dim=0)
        scaled_dot_product  = torch.matmul(x1_expand, x2.transpose(-2, -1)) / (self.inv_scale ** 0.5)
        attention_weights = scaled_dot_product.softmax(dim=-1)
        # (batch_size, heads * head_dim)
        output           = attention_weights.matmul(x2).reshape(x2.shape[0], self.heads, -1)
        return output


# Initializing the model
m = Model()


# Inputs to the model
key   = torch.randn(4, 3, 64, 64)
value = torch.randn(4, 8, 64, 64)
