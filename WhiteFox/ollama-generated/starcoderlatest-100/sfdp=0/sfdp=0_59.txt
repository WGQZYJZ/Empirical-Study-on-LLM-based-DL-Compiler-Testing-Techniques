
class Model(torch.nn.Module):
    def __init__(self, hidden_dim, inv_scale):
        super().__init__()
        self.inv_scale = inv_scale
        self.attention_head = torch.nn.Linear(hidden_dim * 3, hidden_dim)
 
    def forward(self, query, key, value):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / self.inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(value)
        return output


# Initializing the model
m = Model(hidden_dim=3072, inv_scale=1.0 / 4.0)

# Inputs to the model
x1 = torch.randn(8, 512, 16, 16)
q = torch.randn(8, 512, 16, 16)
k = torch.randn(8, 512, 16, 16)
v = torch.randn(8, 512, 16, 16)
