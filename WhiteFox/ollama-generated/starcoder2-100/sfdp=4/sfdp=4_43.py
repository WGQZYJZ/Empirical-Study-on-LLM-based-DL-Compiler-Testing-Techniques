
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1): # Forward pass: query * key' * attn_mask' + value
        q = x1  # 64x3x256
        k = torch.zeros(q)  # 64x3x256

        mask = torch.full((10,1), float('-inf'))
        mask[7] = -float('Inf')

        q_t = q @ k.transpose(-2,-1).reshape(64*8, 256) / math.sqrt(q.size(-1)) + mask 
        attn_weight = torch.softmax(q_t, dim=-1).reshape(64,3,8)
        v  = x1.transpose(-2,-1)[..., :attn_weight.shape[-1]] # 64x3x8
        output  = (attn_weight @ v + 0.5*v)**0.7071067811865476
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1,3,256)
x2  = torch.zeros(1,3,256)

