
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, q_k_v):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        scaled_dot_product = torch.matmul(q_k_v[0], q_k_v[1].transpose(-2, -1)) / q_k_v[2]
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(q_k_v[3])
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
query = torch.randn(8, 3, 64, 64)
key = torch.randn(8, 3, 64, 64)
scale = torch.tensor([57322915])
v_attn = [scaled_dot_product, attention_weights, scaled_dot_product, v6]
