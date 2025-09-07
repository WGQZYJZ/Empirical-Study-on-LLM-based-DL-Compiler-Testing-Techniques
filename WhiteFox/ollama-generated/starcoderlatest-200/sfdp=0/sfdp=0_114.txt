
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, scale=None):
        attention_weights = torch.matmul(query, key.transpose(-2, -1)) / (scale * scale)
        attention_weights  = attention_weights.softmax(dim=-1)
        output = torch.matmul(attention_weights, value)
        return output

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc_query   = torch.nn.Linear(512, 1024)
        self.conv1d     = torch.nn.Conv1d(512, 64, kernel_size=3, stride=1, padding=1)
        self.self_attention = ScaledDotProductAttention()
 
    def forward(self, x):
        q   = self.fc_query(x)
        v   = self.conv1d(q)
        out = self.self_attention(q, v, v, scale=512**0.5)
        return out

# Initializing the model
m = Model()

# Inputs to the model
input_ids = torch.randn((1, 32))
x = input_ids.unsqueeze(-1).permute(0, 2, 1)
