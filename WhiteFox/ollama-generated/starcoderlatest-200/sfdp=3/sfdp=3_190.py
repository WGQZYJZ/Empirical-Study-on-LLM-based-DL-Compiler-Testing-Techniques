
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1024, 512)
 
    def forward(self, query_tensor, key_tensor, value_tensor, scale_factor):
        v1 = self.linear(query_tensor).unsqueeze(dim=-2)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        scaled_qk = v6.mul(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.1)
        output = v6.matmul(dropout_qk).transpose(-2, -1) * value_tensor  # Compute the dot product of the dropout output and the value tensor
        return v6


# Initializing the model
m = Model()
# Inputs to the model
q = torch.randn(10, 1024, 8)
k = torch.randn(10, 1024, 8)
v = torch.randn(10, 512, 64)
scale_factor = 1 / math.sqrt(v.shape[-1])
