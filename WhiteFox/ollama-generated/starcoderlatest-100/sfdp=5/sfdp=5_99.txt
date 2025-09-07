
class Model(torch.nn.Module):
    def __init__(self, query_dim, key_dim, num_heads, num_layers):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

        # Self-Attention Layer
        self.layer_norm = nn.LayerNorm(self.conv.in_channels, eps=1e-12, elementwise_affine=True)

        # MLP Layer for query and key
        self.mlp = nn.Sequential(nn.Conv2d(key_dim, 4 * num_heads, kernel_size=3, stride=1, padding=1),
                                nn.BatchNorm2d(4 * num_heads),
                                nn.ReLU(),
                                nn.AdaptiveMaxPool2d((1, 1)),
                                nn.Conv2d(4 * num_heads, key_dim, kernel_size=1, stride=1, padding=0))

        # MLP Layer for value
        self.mlp_value = nn.Sequential(nn.Conv2d(key_dim, 4 * num_heads, kernel_size=3, stride=1, padding=1),
                                       nn.BatchNorm2d(4 * num_heads),
                                       nn.ReLU(),
                                       nn.AdaptiveMaxPool2d((1, 1)),
                                       nn.Conv2d(4 * num_heads, key_dim, kernel_size=1, stride=1, padding=0))

        # MLP Layer for attention mask
        self.mlp_attn = nn.Sequential(nn.Linear(key_dim * num_heads, 4 * num_heads),
                                      nn.BatchNorm2d(4 * num_heads),
                                      nn.ReLU(),
                                      nn.Dropout2d())

    def forward(self, x1):
        v1 = self.conv(x1)

        # Self-Attention Layer
        q = self.layer_norm(v1)  # Normalizing the input tensor to improve stability.
        k = self.mlp(q)  # Applying MLP to compute the key of the query tensor
        qk = torch.matmul(q, k) / math.sqrt(k.size(-1))  # Compute the dot product of the query and key, scale it

        # Attention Mask Layer
        v = self.mlp_value(qk)
        attn_mask = self.mlp_attn(v).unsqueeze(dim=-2).unsqueeze(dim=-1)  # The input tensor needs to be unsqueezed for broadcasting

        # Self-Attention Layer
        output = torch.matmul(attn_mask, qk)  # Compute the dot product of the attention mask and scaled dot product
        return output
# Initializing the model
m = Model(key_dim=4, query_dim=4, num_heads=1, num_layers=8)


