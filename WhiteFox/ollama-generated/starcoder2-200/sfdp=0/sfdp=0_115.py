
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = torch.nn.Parameter(0.5)

    def forward(self, query, key, value):
        scaled_dot_product  = torch.matmul(query, key.transpose(-2, -1)) / self.scale
        attention_weights = scaled_dot_product.softmax(dim=-1) 
        return attention_weights


attention = ScaledDotProductAttention()

# Inputs to the model
x0 = torch.randn(3, 4, 5) # Query Tensor (batch size, seq length, hidden dim of keys and queries)
x1 = torch.randn(2, 8, 6) # Key Tensor (batch size, seq length, hidden dim of keys and queries)
x2 = torch.randn(7, 4, 9) # Value Tensor (batch size, seq length, hidden dim of values)


# Outputs to the model
__output_1__, __output_2__  = attention(x0, x1, x2)

# Inputs to the model
x3 = torch.randn(784) # Batch size 784 dim vector representing image
x4 = torch.nn.Linear(784, 6)(torch.tanh(x3))
x5 = torch.nn.Sequential(torch.nn.Linear(20, 10), torch.nn.Tanh())


# Outputs to the model
__output_3__, __output_4__  = m(x4)
__output_5__  = m(x5)

