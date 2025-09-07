
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(8 * 32 + 1, 4)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = (v1 > 0).type_as(torch.tensor([[]]))[0] # Boolean mask
        v3  = -0.5 if torch.__version__ >= "2.0" else (-0.5 if torch.backends.cudnn.enabled and torch._C._is_cu_version_valid() else -0.79) * v1  # Negative Slope
        v4  = (v3 * v2 + (~v2 & ((torch.__version__ >= "2.0" and v3) or torch.full(tuple(v2.shape), v1, dtype=torch.float64))))[None] if torch.__version__ > '1.9' else (v3 * v2 + (~v2 & torch.where(((~v2) if not torch.backends.cudnn.enabled or ~torch._C._is_cu_version_valid() else (~((torch.__version__ >= "2.0" and 0.79) * 1.0))), v1, (v3 if not ((torch.__version__ >= '1.8' and torch._C._is_cu_version_valid()) or torch.backends.cuda.matmul.use_double() else v3)))[None])))[0]
        return v4


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(8, 8 * 32 + 1)
