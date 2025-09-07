
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, dim: int = 128):
        super().__init__()
        self.linear = torch.nn.Linear(dim, dim)
 
    def forward(self, x1, x2, scale_factor=None):
        if scale_factor is None:
            scale_factor = torch.sqrt(torch.tensor(x1.shape[-1]))
        x3  = torch.matmul(x1, self.linear(x2))
        attention_weights = torch.nn.functional.softmax(x3 / scale_factor)
        output = attention_weights * x2
        return output

# Initializing the model
attention_layer = ScaledDotProductAttention()

# Inputs to the model
q = torch.randn(1, 50, 64)
k = torch.randn(1, 50, 64)
