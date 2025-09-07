
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(value)
        return output


# Initializing the model
m = Model()


# Inputs to the model
query = torch.randn(2, 3, 64, 64) # Query tensor is a batch of queries. Each query consists of the same number of dimensions and has shape (B, H, W, C). 
key = torch.randn(2, 8, 64, 64) # Key tensors are usually learned to predict the values that the keys map to. The number of channels of key/value should be equal.
inv_scale = math.sqrt(8.0 / (3.0 + key.size(-1))) # Here we use a special technique called "scaling normalization" for computing the scaling factor in this step.
