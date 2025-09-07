
class Model(torch.nn.Module):
    def __init__(self, heads, embed_dim):
        super().__init__()
 
        self.heads = heads  # Number of head/head pairs to use
        self.scale = (embed_dim // heads) ** -0.5

        self.to_qkv = torch.nn.Linear(32 * 32, 32 * 3 * heads, bias=False)

    def forward(self, x): # Batch size: N, Number of channels: C, Height and Width of images: H, W
        qkv = self.to_qkv(x).permute([0, 1, 3, 2, 4]) # Shape: (B, N/H*W*C, 3, heads)

        query, key, value = qkv[...,:self.heads], qkv[...,self.heads:2*self.heads], qkv[...,2*self.heads:]

        return torch.matmul(query, key.transpose(-2, -1))


# Inputs to the model
q  = torch.randn(16, 32 * 8, 8, 8)  # Shape: (B, C/h, h, w), where h and w are height and width of the image in pixels, c is number of channels and h and w are numbers of heads
v  = torch.randn(16, 32 * 8, 4, 4)  # Shape: (B, C/h, h, w), where h and w are height and width of the image in pixels, c is number of channels and h and w are numbers of heads
x1 = torch.cat([q, v], dim=0) # Concatenate the query tensor with the value tensor along dimension 0

