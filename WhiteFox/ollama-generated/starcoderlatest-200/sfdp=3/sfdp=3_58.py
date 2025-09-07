
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.key   = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, query, key):
        v_qk = torch.matmul(query, key.transpose(-2,-1))
        v_scaled_qk = v_qk * scale_factor
        v_softmax_qk = torch.nn.functional.softmax(v_scaled_qk, dim=-1)
        v_dropout_qk = torch.nn.functional.dropout(v_softmax_qk, p=0.3)
        output = torch.matmul(v_dropout_qk, value)
        return output

# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(1, 3, 64, 64)
key   = torch.randn(1, 8, 64, 64)
