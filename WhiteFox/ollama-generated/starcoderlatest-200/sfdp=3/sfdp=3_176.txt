
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.matmul_attention = torch.nn.Linear(64, 128) # Linear layer with dimension 64 and output size 128

    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        attention = self.matmul_attention(output)

        return attention


# Initializing the model
m = Model()
# Inputs to the model
query = torch.randn(128, 3, 64, 64)
key   = torch.randn(128, 3, 64, 64)
value = torch.randn(128, 3, 64, 64)


