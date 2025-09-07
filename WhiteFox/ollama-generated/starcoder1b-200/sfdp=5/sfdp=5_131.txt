
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(16, 8)
        self.key   = torch.nn.Linear(8, 8)
        self.value = torch.nn.Linear(8, 32)
        self.dropout = 0.5
 
        # The linear operations are not shared
        self.attention_softmax = None
 
    def forward(self, x1):
        q = self.query(x1).unsqueeze(-2).unsqueeze(-1) # (batch_size, seq_len, depth, width)
        k = self.key(x1).unsqueeze(-3).unsqueeze(-1) # (batch_size, seq_len, depth, width)
        v = self.value(x1).unsqueeze(0).unsqueeze(-2)  # (batch_size, seq_len, width, depth)
        attention_softmax = self.attention_softmax(q @ k.transpose(-2, -1), dim=-2)
        attn_weight = torch.dropout(attention_softmax, self.dropout, True)
        output = attn_weight @ v
        return output

# Initializing the model
m = Model()


