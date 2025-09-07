
class Model(torch.nn.Module):
    def __init__(self, inv_scale=None):
        super().__init__()
        self.query = torch.nn.Linear(8 * 64, 128)
        self.key = torch.nn.Linear(8 * 64, 128)
        self.value = torch.nn.Linear(8 * 64, 128)
 
        if inv_scale is None:
            inv_scale = 8 * 64
 
    def scaled_dot_product_attention(self, x):
        query = torch.nn.functional.linear(x, self.query, bias=None)
        key = torch.nn.functional.linear(x, self.key, bias=None)
 
        value = torch.nn.functional.linear(x, self.value, bias=None)
        scaled_dot_product = query @ key.transpose(-2, -1) / math.sqrt(inv_scale)
 
        attention_weights = torch.softmax(scaled_dot_product, dim=-1)
 
        output  = attention_weights.matmul(value)
        return output
 
    def forward(self, x):
        return self.scaled_dot_product_attention(x)


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(2, 3, 64, 64)
