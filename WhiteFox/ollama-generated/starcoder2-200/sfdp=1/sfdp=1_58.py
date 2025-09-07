
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query1: torch.Tensor, key2: torch.Tensor, value3: torch.Tensor) -> torch.Tensor:
        v1  = torch.matmul(query1, key2.transpose(-2,-1))
        v4  = torch.nn.functional.dropout(v1, p=0.5)
        v6  = v4 + value3
        return v6

