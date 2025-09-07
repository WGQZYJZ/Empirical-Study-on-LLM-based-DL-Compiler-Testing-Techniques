
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_1 = torch.nn.Linear(64, 8)
        self.attn_2 = torch.nn.Linear(16, 8)
 
    def forward(self, qk, v, attn_mask=None):
        if attn_mask is not None:
            attn_mask = attn_mask.unsqueeze(0).unsqueeze(-1)
            attn_mask = torch.nn.functional.softmax(attn_mask, dim=-2) * -1e9 + 1
        else:
            attn_mask = torch.ones((qk.shape[0], qk.shape[-1]), device=qk.device)
 
        v = torch.transpose(v, -2, -1) # permute the dimensions of `q` and `kv`, where `-2` is the first axis (batch), `-1` is the second axis (feature dimension).
        attn_weight  = torch.nn.functional.softmax(qk @ v / math.sqrt(qk.size(-1)), dim=-2) * -1e9 + 1 # softmax of the scaled dot product of the query and key, followed by a mask
        output = torch.nn.functional.dropout(attn_weight @ v, p=0.8, training=self.training) # dropout operation on attn_weights * v
        return output


# Initializing the model
m = Model()


# Inputs to the model
qk  = torch.randn(128, 3, 64, 64)
v = torch.randn(128, 8, 64, 64)
attn_mask = torch.ones((128, 1), device=qk.device)
