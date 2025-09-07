
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32768, 32)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        scaled_dot_product = torch.matmul(v1, v1.transpose(-2, -1)) / inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(value)
        return output

# Initializing the model
m = Model()
# Inputs to the model
x1 = torch.randn(2, 32768)
