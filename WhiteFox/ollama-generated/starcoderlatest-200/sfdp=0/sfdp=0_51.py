
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.Linear(3 * 64 * 64, 8 * 128)
        self.value = torch.nn.Linear(8 * 128, 8)
 
    def forward(self, q, k, v):
        scaled_dot_product = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(k.shape[-1])
        attention_weights = F.softmax(scaled_dot_product, dim=-1)
        output  = attention_weights.matmul(v)
        return output

# Initializing the model
m = Model()

# Inputs to the model
q = torch.randn(8, 3 * 64 * 64)
k = torch.randn(8, 3 * 64 * 64)
v = torch.randn(8, 8 * 128)
