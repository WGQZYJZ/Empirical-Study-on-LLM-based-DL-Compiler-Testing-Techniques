
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.dim = dim
 
    def forward(self, q1, k1, v1):
        dot_product = torch.matmul(q1, k1.transpose(-2, -1)) / self.dim**0.5
        attention_weights = torch.softmax(dot_product, dim=-1)
        output = attention_weights.matmul(v1)
        return output

# Inputs to the model
q1 = torch.randn(1, 32, 768, 768)
k1 = torch.randn(192, 32, 768, 768)
v1 = torch.randn(192, 32, 768, 768)
