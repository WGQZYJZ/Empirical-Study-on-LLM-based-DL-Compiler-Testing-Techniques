The function `ScaledDotProductAttention` in the file is used to compute the attention weights between a query tensor and a key tensor based on the Scaled Dot Product Attention mechanism, which also includes some parameters, e.g., the dimension of the query and value tensors. The computation steps are shown as follows:
1. Apply a linear transformation (`self.scale_factor * torch.nn.Linear(dim_key, dim_value, bias=False)`), then use `torch.matmul` to compute the scaled dot-product between query and key tensor;
2. Use the softmax of the results as the attention weights;
3. Apply a linear transformation (`self.scale_factor * torch.nn.Linear(dim_value, dim_value, bias=False)`) to calculate a weighted sum of the value tensors according to the attention weights and return this weighted tensor.
