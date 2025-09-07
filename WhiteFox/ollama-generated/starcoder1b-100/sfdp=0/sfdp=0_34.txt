
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1, query, key, value):
        v1 = self.conv(x1)
        inv_scale = torch.sqrt(torch.tensor([query.shape[-1], key.shape[0]], dtype=torch.float32)).unsqueeze(-1).expand(*query.shape[:2]).to(device)
        attention_weights = torch.matmul(v1, query).div_(inv_scale).softmax(dim=-1)
        v2 = torch.matmul(attention_weights, value)
        return v2


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
query  = torch.randn(8, 16, 16, 3)
key   = torch.randn(8, 16, 16, 3)
value = torch.randn(16, 32, 32, 8)
