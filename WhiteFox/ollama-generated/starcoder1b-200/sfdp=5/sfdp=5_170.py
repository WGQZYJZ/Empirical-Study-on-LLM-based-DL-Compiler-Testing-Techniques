
class Model(torch.nn.Module):
    def __init__(self, d_model):
        super().__init__()
        self.d_model = d_model
        self.key_weight = torch.nn.Linear(d_model, d_model)
        self.value_weight = torch.nn.Linear(d_model, d_model)
 
    def forward(self, input):
        # Use transpose to swap keys and values since they're transposed in the paper
        # (https://arxiv.org/abs/1706.03762)
        query, key = input.split([self.d_model // 4, self.d_model // 4], dim=-1)
        attn = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(input.size(-1))
        attn = F.softmax(attn, dim=-1)
        value = torch.matmul(attn, input)
        return value


# Inputs to the model
x  = torch.randn(32, 1024)
