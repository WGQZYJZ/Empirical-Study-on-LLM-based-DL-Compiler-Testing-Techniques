
class Model(torch.nn.Module):
    def __init__(self, scale_factor=10):
        super().__init__()
        self.scale_factor = scale_factor

    def forward(self, query, key, value):
        inv_scale  = math.sqrt(self.scale_factor)
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / inv_scale

        attention_weights = torch.softmax(scaled_dot_product, dim=-1)
        output = attention_weights.matmul(value)
        return output


# Initializing the model
m  = Model()


# Inputs to the model
query = torch.randn(20, 36, 64, 64)  # The input of a query is always a tensor with shape [batch_size x seq_length x channels]
key = torch.randn(19, 15, 64, 64)    # When computing attention weights, the attention weights are computed as softmax on scaled dot product of query and key. The attention weights are then used to compute a weighted sum of value, which is usually just the value itself.
value = torch.randn(20, 36, 10, 1)   # The input of a value is always a tensor with shape [batch_size x seq_length x channels]
__output__  = m(query, key, value)


