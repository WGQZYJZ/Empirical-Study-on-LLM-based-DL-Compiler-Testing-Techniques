
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, query, key, value, scale_factor, dropout_p):
        v1 = self.conv(query)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk / scale_factor
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output
 
 # Initializing the model
m = Model()

 # Inputs to the model
query  = torch.randn(32, 3, 64, 64)
key    = torch.randn(32, 8, 192, 192)
value  = torch.randn(32, 8, 192, 192)
scale_factor  = torch.randn(())
dropout_p  = torch.randn(())

 