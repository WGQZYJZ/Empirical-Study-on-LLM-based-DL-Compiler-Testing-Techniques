
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(3, 8)
        self.key   = torch.nn.Linear(3, 8)
 
    def forward(self, query_tensor, key_tensor):
        qk = torch.matmul(query_tensor, key_tensor.transpose(-2, -1))
        scaled_qk = qk / (inv_scale_factor ** (0.5))
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = F.dropout2d(softmax_qk, dropout=dropout_p) # dropout applies to a specific dimension only
        output = torch.matmul(dropout_qk, value)  # Compute the dot product of the dropout output and the value
        return output


# Initializing the model
m = Model()
q1 = torch.randn(4, 3, 64, 64)
k1 = torch.randn(5, 3, 64, 64)
v1 = torch.randn(6, 3, 64, 64)
query_tensor = q1[:, :3].reshape((4, -1)) # the value of q1 is in q1[:3] and the rest of q1 will be zero
key_tensor   = k1[:, :3].reshape((5, -1))
__output__  = m(query_tensor, key_tensor)


