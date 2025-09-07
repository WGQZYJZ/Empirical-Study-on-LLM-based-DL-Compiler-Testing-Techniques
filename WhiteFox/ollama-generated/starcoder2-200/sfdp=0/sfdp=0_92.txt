
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, inv_scale: float = 64):
        super().__init__()

        self.softmax  = torch.nn.Softmax(dim=-1)

    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor):
 
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(key.shape[-1])
        attention_weights  = self.softmax(scaled_dot_product)

        output             = torch.bmm(attention_weights, value)

        return output
