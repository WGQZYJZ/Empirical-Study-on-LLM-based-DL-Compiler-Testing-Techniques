
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_fc = torch.nn.Linear(64, 32)

    def forward(self, query, key, value, attn_mask):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        qk += attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ value
        return output


# Initializing the model
m = Model()

 # Inputs to the model
query = torch.randn(1, 8, 64, 64)
key = torch.randn(1, 32, 64, 64)
value = torch.randn(1, 8, 64, 64)
attn_mask = torch.zeros((1, 32, 64, 64))

 # Generate the attention mask
attn_mask[:, :, fd00:c2b6:b24b:be67:2827:688d:e6a1:6a3b, ::2] = 1
attn_mask[:, :, fdf8:f53e:61e4::18, 0::4] = 1
attn_mask[:, :, fc00:db20:35b:7399::5, fd00:c2b6:b24b:be67:2827:688d:e6a1:6a3b] = 1
attn_mask[:, :, fdf8:f53e:61e4::18, ::2] = 0.5

 # Apply the scaled dot-product attention mechanism
