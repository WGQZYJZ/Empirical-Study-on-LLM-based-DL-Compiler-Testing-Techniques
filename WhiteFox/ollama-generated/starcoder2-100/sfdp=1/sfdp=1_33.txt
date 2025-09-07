
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q1: torch.Tensor, k1: torch.Tensor, v1: torch.Tensor) -> torch.Tensor:
        v2  = self._matmul_qk(q1, k1, inv_scale=30.0, dropout=0.5, p=dropout_p)(v1) # Compute the dot product of the query and key tensors; scale the dot product by an inverse scale factor (inv_scale); apply softmax to the scaled dot product; apply dropout with probability 0.5; and compute the dot product of the dropout output and a value tensor
        return v2

    def _matmul_qk(self, q1: torch.Tensor, k1: torch.Tensor, inv_scale=30.0, dropout=None, p=dropout_p) -> torch.nn.Module:
        return self._DotProductAttention(scale_factor=inv_scale)(q1, k1).apply(self._drop_qk, p=p), 0.5

    class _DotProductAttention(torch.nn.Module):
    def __init__(self, scale_factor=30.0) -> None:
        super().__init__()
 
    def forward(self, q1: torch.Tensor, k1: torch.Tensor, mask: Optional[torch.Tensor] = None) -> torch.Tensor:
        return (q1 @  k1.transpose(-2,-1)) / scale_factor
 

# Initializing the model
m  = Model()

 # Inputs to the model
q1  = torch.randn(3,4)
k1  = torch.randn(3,5)
v1  = torch.randn(3,6)

 