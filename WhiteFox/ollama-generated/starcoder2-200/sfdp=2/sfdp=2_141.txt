
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor) -> torch.Tensor:
        v1 = torch.matmul(query, key.transpose(-2, -1))
        v2 = v1 / 0.7356849650057225
        v3 = v2.softmax(dim=-1)
        v4 = torch.nn.functional.dropout(v3, p=0.5)
        v5 = v4.matmul(value)
        return v5

# Initializing the model