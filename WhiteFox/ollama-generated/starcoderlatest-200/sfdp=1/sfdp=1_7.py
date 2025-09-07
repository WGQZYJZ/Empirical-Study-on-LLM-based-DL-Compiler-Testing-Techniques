
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_q = torch.nn.Linear(3, 8)
        self.linear_k = torch.nn.Linear(256, 1024)
 
    def forward(self, q1, k1):
        v1 = self.linear_q(q1) * (k1.div(self.scale_factor).softmax(dim=-1))
        return torch.matmul(v1, self.linear_k.transpose(-2, -1)).mul_(self.value_scaling)
 
    def set_scale_factor(self, scale_factor):
        self.scale_factor = scale_factor
