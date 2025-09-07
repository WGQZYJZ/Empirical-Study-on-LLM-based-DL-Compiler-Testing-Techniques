m = nn.Sequential(
    torch.nn.Conv2d(32 * query_dim, 64 * attention_heads * head_dim, 1),
    torch.nn.ReLU(),
    torch.nn.BatchNorm2d(64 * attention_heads * head_dim)
)
qk = m(query).transpose(-2, -1) # [b, nh, nq, sdim]
