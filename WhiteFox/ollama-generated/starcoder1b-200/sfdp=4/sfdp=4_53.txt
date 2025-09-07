
class Model(torch.nn.Module):
    def __init__(self, query_dim=256, attn_dim=4096, num_heads=8):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.query = torch.nn.Linear(query_dim, attn_dim)
        self.value = torch.nn.Linear(attn_dim, query_dim)
        self.key = torch.nn.Linear(query_dim, attn_dim)
        self.attn = torch.nn.Linear(attn_dim, attn_dim, bias=False)

    def forward(self, x1):
        batch_size, n_channels, _, _ = x1.shape
        q = self.query(x1).view(batch_size * n_channels, -1)  # N x D x H x W
        k = self.key(x1).view(batch_size * n_channels, -1)
        v = self.value(x1).view(batch_size * n_channels, -1)
        weights = torch.bmm(q, k.transpose(-2, -1)) / math.sqrt(k.size(-1))  # N x D x H x W
        attentions = F.softmax(weights, dim=-1)  # N x D x H x W
        context = self.conv(x1).view(batch_size * n_channels, -1,
                                      self.attn(weights).shape[2],
                                      self.attn(weights).shape[3])  # N x (D * H * W) x H x W
        context *= attentions  # N x (D * H * W) x H x W
        return context


# Initializing the model
m = Model()

