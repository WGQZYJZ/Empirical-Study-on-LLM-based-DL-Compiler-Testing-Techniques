
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.Linear(10, 8)
 
    def forward(self, query, key, value, scale_factor, dropout_p):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output


# Initializing the model
m = Model()

# Inputs to the model
query  = torch.randn(20, 10, 768)
key    = torch.randn(30, 10, 768)
value  = torch.randn(40, 10, 768)
scale_factor = 30 ** 0.5 # Scale the dot product by a factor of sqrt(30)
dropout_p     = 0.5   # Apply dropout with probability 0.5
