
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, num_heads: int = 8, dim: int = 128, attn_mask: torch.Tensor = None):
        super().__init__()
        self.num_heads = num_heads # number of attention heads to use
        self.dim = dim # size of the feature vectors for all heads

        qkv_linear = nn.Linear(dim, 3 * dim)

        self.q_proj = nn.Conv2d(3, num_heads, 1, stride=1, padding=0) 
        self.k_proj = nn.Conv2d(3, num_heads, 1, stride=1, padding=0)
        self.v_proj = nn.Conv2d(3, num_heads, 1, stride=1, padding=0)

        attn_linear = nn.Linear(dim, dim)

        if attn_mask is not None:
            mask_proj = nn.Conv2d(1, 1, 1, stride=1, padding=0)
        else:
            mask_proj = None

        self.attn_proj = nn.Sequential(mask_proj, qkv_linear, nn.ReLU(), attn_linear, nn.Softmax(dim=-1), )

        if num_heads > 1:
            self.scale_head = dim ** -0.5

    def forward(self, input):
        