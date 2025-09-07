
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.key = torch.nn.Linear(64, 64)
        self.query = torch.nn.Linear(64, 64)
        self.value = torch.nn.Linear(64, 64)
 
    def forward(self, x1):
        qk  = torch.matmul(x1, self.key.weight).unsqueeze(-2) + torch.matmul(x1, self.query.weight)
        scaled_dot_product = qk / inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output  = attention_weights.matmul(self.value.weight)
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 64, 32, 32)
