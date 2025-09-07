

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layer = torch.nn.Linear(3, 1)

    def forward(self, query: Tensor, key: Tensor, value: Tensor) -> Tensor:
        scale_factor = get_scale()

        attn = torch.matmul(query, key.transpose(-2, -1)) / scale_factor

        attn = attn.softmax(dim=-1)

        attn = torch.nn.functional.dropout(attn, p=0.5)

        out = (attn * value).sum(dim=1)
        return self.layer(out)


model = Model()

query = torch.randn(4, 3)
key = torch.randn(4, 3)
value = torch.randn(4, 5)

