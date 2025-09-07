
# Initializing the model
m  = Model()

# Inputs to the model
query  = torch.randn(64, 3072)
key    = query.clone().view(1, -1, 8) / math.sqrt(8) + 1e-5
value  = key[:, :, None].repeat_interleave(32, dim=1).permute(1, 0, 2)

