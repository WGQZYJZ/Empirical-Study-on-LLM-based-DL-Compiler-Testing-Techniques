
class Model(torch.nn.Module):
    def __init__(self, q, k, v, scale_factor=100.0, dropout_p=0.5):
        super().__init__()
        self.scale_factor = torch.tensor([float(scale_factor)], dtype=torch.float32).cuda() if not isinstance(scale_factor, torch.Tensor) else scale_factor
        self.dropout = torch.nn.Dropout(p=float(dropout_p))
 
        self.qkv  = torch.nn.Linear(in_features=int(q), out_features=3*int(k), bias=True)
 
    def forward(self, x1):
        v1  = self.qkv(x1).chunk(3, dim=-1)
        v2  = [v.mul(scale_factor).softmax(-1) for v in v1] # Scaled qk: [softmax(qk) * scale_factor]
        dropout_qk  = [torch.nn.functional.dropout(v[0], p=float(self.dropout)) for v in zip(v2, self.qkv(x1))] # Dropout
        v3  = torch.stack([d.matmul(v) for d, v in zip(dropout_qk, v1)], dim=-2)
        return v3


# Initializing the model