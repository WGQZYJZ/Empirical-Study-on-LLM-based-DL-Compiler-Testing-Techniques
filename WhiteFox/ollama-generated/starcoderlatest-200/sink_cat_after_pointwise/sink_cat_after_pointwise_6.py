
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        t1 = torch.cat([x1, x2], dim=1) # Permute the inputs to concatenate along dim 1
        t2 = t1.view(-1, 8)            # Reshape to (batch_size * n_elements * input_dim)
        return torch.relu(t2)          # Relu only uses one of the concatenated dimensions


# Input tensor shapes for testing sink_cat_after_pointwise optimization
x1 = torch.randn(2, 4, 3, 5, dtype=torch.float64)
x2 = x1 + x1
m = Model()
