
class Model(torch.nn.Module):
    def __init__(self, input_dim=1024):
        super().__init__()
        self.dropout = torch.nn.Dropout()
        self.linear_q = torch.nn.Linear(input_dim, 8, bias=True)
        self.linear_k = torch.nn.Linear(input_dim, 8, bias=True)
        self.linear_v = torch.nn.Linear(input_dim, 32, bias=True)
 
    def forward(self, q1, k1, v1):
        dot_product = torch.matmul(q1, k1.transpose(-2, -1))
        inv_scale_factor = (float(1.0) / self.linear_k.weight[3]) ** 0.5
        scaled_dot_product = dot_product * inv_scale_factor
        softmax_scaled_dot_product = scaled_dot_product.softmax(-1)
        dropout_scaled_softamx_dot_product = torch.nn.functional.dropout(softmax_scaled_dot_product, p=0.2)
        output = dropout_scaled_softamx_dot_product.matmul(v1)
        return output


# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(5, 32, 64, 64) # (batch_size, n_heads, qkv_dim1, qkv_dim2)
key = torch.randn(5, 32, 64, 64)
value = torch.randn(5, 32, 64, 64)


