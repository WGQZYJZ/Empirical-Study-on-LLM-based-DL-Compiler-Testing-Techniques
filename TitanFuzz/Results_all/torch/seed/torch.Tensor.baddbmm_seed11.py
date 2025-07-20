batch_size = 3
n_features = 5
input_tensor = torch.randn(batch_size, n_features)
batch1 = torch.randn(batch_size, n_features, n_features)
batch2 = torch.randn(batch_size, n_features, n_features)
result = torch.Tensor.baddbmm(input_tensor, batch1, batch2)