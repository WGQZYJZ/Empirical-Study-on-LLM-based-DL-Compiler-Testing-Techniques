
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.q  = torch.nn.Linear(3, 64)
        self.k  = torch.nn.Linear(3, 128)
        self.v  = torch.nn.Linear(3, 128)
        self.scale_factor = math.sqrt(self.k.out_features / self.q.out_features)
 
    def forward(self, query, key, value):
        v = (query @ key.transpose(-2, -1)) * self.scale_factor
        q  = query @ torch.nn.functional.softmax(key, dim=-1).unsqueeze(-1)
        k  = key  @ torch.nn.functional.softmax(value, dim=-1).unsqueeze(-1)
        return v @ q
 
    def forward_torch(self, x1):
        m1 = self.q(x1)
        m2 = self.k(x1)
        m3 = self.v(x1)
        return m1 @ torch.nn.functional.softmax(m2).unsqueeze(-1) @ m3
 
    def forward_torch_v2(self, x1):
        q = self.q(x1)
        k = self.k(x1)
        v = (q @ k.transpose(-2, -1)) * torch.sqrt((k.out_features / q.out_features).view(1, 1, -1)).unsqueeze(-1)
        return torch.matmul(v, torch.nn.functional.softmax(k, dim=-1).unsqueeze(-1)) @ v
 
 
# Initializing the model
m = Model()


