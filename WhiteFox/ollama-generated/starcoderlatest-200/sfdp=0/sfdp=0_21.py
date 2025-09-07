
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scaled_dot_product = torch.nn.ScaledDotProduct(num_dimensions=1)
 
    def forward(self, query, key, value, inv_scale):
        v  = self.scaled_dot_product(query, key, dim=-1) / inv_scale
        attention_weights = torch.softmax(v, dim=-1)
        output  = attention_weights.matmul(value)
        return output


# Initializing the model
m = Model()

# Inputs to the model
queries = torch.randn(3, 64, 64)
keys = torch.randn(8, 64, 64)
values = torch.randn(8, 64, 64)
inv_scales = torch.randn(8, dtype=torch.float) * 0.5
