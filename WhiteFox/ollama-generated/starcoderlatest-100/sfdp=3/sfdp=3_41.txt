
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.key_q = torch.nn.Parameter(
            torch.randn(8, 64, 16, 2, dtype=torch.float32), requires_grad=True)
 
    def forward(self, query, key, scale_factor):
        v1 = torch.matmul(query, self.key_q)
        v2 = v1 * scale_factor
        softmax_qk = torch.nn.functional.softmax(v2, dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.5)
        output = dropout_qk.matmul(key)
        return output


# Initializing the model
m = Model()

# Inputs to the model
query  = torch.randn(1, 3, 64, 2, dtype=torch.float32)
key  = torch.randn(8, 3, 64, 2, dtype=torch.float32)
scale_factor  = torch.rand(dtype=torch.float32) + 1e-5
