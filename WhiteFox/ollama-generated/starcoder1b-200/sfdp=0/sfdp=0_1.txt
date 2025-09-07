
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        query_weight, value_weight = self._build_attention(x1, x2)
        scaled_dot_product = torch.matmul(query_weight, key_weight.transpose(-2, -1)) / inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(value_weight)
        return output
 
    def _build_attention(self, x1, x2):
        query_weight  = self.conv(x1)
        query_scale    = torch.nn.functional.softplus(-torch.mean(query_weight, dim=-1).reshape(1, -1))
        query_weight  *= query_scale
        key_weight     = self.conv(x2)
        key_scale      = torch.nn.functional.softplus(-torch.mean(key_weight, dim=-1).reshape(1, -1))
        key_weight     *= key_scale
        inv_scale      = torch.sqrt(torch.mean(key_weight, dim=-1)) * query_scale  # Scale the attention weights along the batch dimension
        return (query_weight, value_weight), inv_scale


# Initializing the model
m = Model()


