
class Model(torch.nn.Module):
    def __init__(self, dim_qkv=512):
        super().__init__()
        self.linear_qk = torch.nn.Linear(dim_qkv, dim_qkv)
 
    def forward(self, qk):
        q  = self.linear_qk(qk[:, :3])
        k  = self.linear_qk(qk[:, 3:6])
        v  = self.linear_qk(qk[:, 6:])
        qk = torch.stack([q, k, v], dim=1)
 
        qk = qk * 0.5
 
        softmax_qk = torch.nn.functional.softmax(qk, dim=-2)
 
        output = softmax_qk.matmul(v)
 
        return output


# Initializing the model and specifying input dimensions
m = Model(dim_qkv=512)
 
# Inputs to the model
x1 = torch.randn(16, 768, 8, 14)
