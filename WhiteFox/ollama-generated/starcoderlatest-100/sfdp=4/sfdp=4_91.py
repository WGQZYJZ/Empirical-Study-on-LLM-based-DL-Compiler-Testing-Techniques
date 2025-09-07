
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.key = torch.nn.Linear(128, 512)
        self.value = torch.nn.Linear(128, 512)
 
    def forward(self, q, k):
        attn_mask = torch.ones(q.shape[0], 1, 14, 14).to('cuda')  # shape: (batch size, 1, sequence length, sequence length)
        v  = self.value(k).transpose(-2, -1)  # (batch size, key features, sequence length, key features)
        v *= attn_mask  # scale the value by the attention mask before applying softmax
        attn_weight = torch.softmax(q @ k.transpose(-2, -1) / math.sqrt(k.shape[-1]), dim=-1)  # (batch size, query features, sequence length, key features)
        output = attn_weight @ v  # (batch size, query features, sequence length, value features)
        return output


# Initializing the model
m = Model()

# Inputs to the model
q = torch.randn(128, 512, 14, 14).to('cuda')
k = torch.randn(128, 512, 36, 36).to('cuda')
