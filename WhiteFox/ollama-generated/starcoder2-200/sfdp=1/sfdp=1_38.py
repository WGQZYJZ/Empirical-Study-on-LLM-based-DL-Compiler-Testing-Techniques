
class Model(torch.nn.Module):
    def __init__(self, key_channels: int=32, value_channels: int=10):
        super().__init__()
        self.key = torch.nn.Linear(in_features=8 * 64**2 + 1000 * 7*7, out_features=key_channels)
        self.scale_factor = key_channels ** -0.5
 
    def forward(self, query):
        v = self._get_value_tensor()
        k = torch.nn.functional.adaptive_avg_pool2d(query[:, None, ...], (7, 7)) # Adaptive average pool of the query
        qk = torch.matmul(torch.flatten(v), k)  # Compute the dot product between the value and the adaptive-pooled query tensors
        scaled_qk  = qk.div(self.scale_factor) # Scale the dot product by self.scale_factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product,
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.5)  # Apply dropout to the softmax output
        return v * dropout_qk.matmul(k)
 
    def _get_value_tensor(self):
        t1 = query[:, None, ...].expand(-1, 7*7, -1) 
        t2 = torch.ones(8 * 64**2 + key_channels * 7*7).view(key_channels, 7*7).transpose(0, 1)
        t3 = self.key(torch.cat((t1, t2), dim=2)) 
        return F.gelu(t3.matmul(query[:, None].transpose(-2, -1)))

