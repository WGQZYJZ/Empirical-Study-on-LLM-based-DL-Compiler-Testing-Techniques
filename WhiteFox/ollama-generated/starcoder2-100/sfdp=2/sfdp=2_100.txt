
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, q1: torch.Tensor) -> torch.Tensor:
        v1 = torch.matmul(q1, k1 * inv_scale_factor).softmax(dim=-1).dropout(p=0.8).matmul(v1)
        return v1


# Initializing the model
m  = Model()

# Inputs to the model
q1 = torch.randn(256, 3*768)
k1 = torch.rand(3*768, 4096) / 3e-4

 