
class SelfAttention(torch.nn.Module):
    def __init__(self, dim: int = 512):
        super().__init__()
        self.query_conv = torch.nn.Conv2d(dim, dim // 8, 1)
        self.key_conv = torch.nn.Conv2d(dim, dim // 8, 1)
        self.value_conv = torch.nn.Conv2d(dim, dim, 3, padding=1)
 
    def forward(self, x):
        query = self.query_conv(x).permute(0, 2, 3, 1)
        key = self.key_conv(x)
        value = self.value_conv(x)
        attention_weights = F.softmax(torch.matmul(query, key.transpose(-2, -1)), dim=-1)
        output = torch.matmul(attention_weights, value)
        return output


# Initializing the model
sa = SelfAttention()

# Inputs to the model
x1 = torch.randn(1, 512, 64, 64)
