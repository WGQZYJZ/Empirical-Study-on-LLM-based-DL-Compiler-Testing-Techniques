x = torch.randn(5, 10)
torch.nn.FeatureAlphaDropout(p=0.5, inplace=False)
feature_alpha_dropout = nn.FeatureAlphaDropout(p=0.5, inplace=False)
x_out = feature_alpha_dropout(x)