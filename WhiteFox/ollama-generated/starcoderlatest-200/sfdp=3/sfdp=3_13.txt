
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale_factor = 1.0 / (3 * math.sqrt(3))
 
    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.mul(self.scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.5)
        output = dropout_qk.matmul(value)
        return output


# Input tensors to the model
query  = torch.randn(2, 3, 64, 64)
key    = torch.randn(1, 3, 64, 64)
value  = torch.randn(2, 8, 64, 64)
