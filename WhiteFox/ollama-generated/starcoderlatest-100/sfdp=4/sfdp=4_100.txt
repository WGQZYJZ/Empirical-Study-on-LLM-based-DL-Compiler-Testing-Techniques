
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(768, 512)
        self.key = torch.nn.Linear(768, 512)
        self.value = torch.nn.Linear(768, 512)
 
    def forward(self, x):
        qk = self.query(x).unsqueeze(dim=1) # (batch_size, heads, length_q, d_head)
        ky = self.key(x).unsqueeze(dim=0)  # (batch_size, heads, length_v, d_head)
        vz = self.value(x) # (batch_size, heads, length_v, d_head)
        qk *= key_scale
        attn_weights = torch.softmax(qk @ ky.transpose(-2, -1) / math.sqrt(qk.size(-1)), dim=-1) # (batch_size, heads, length_q, length_v)
        output = vz * attn_weights
        return output


# Initializing the model
m = Model()


# Inputs to the model
x  = torch.randn(20, 768)  # (batch_size, seq_len, feature_dim)
