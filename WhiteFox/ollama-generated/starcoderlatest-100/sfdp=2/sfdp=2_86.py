
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_q = torch.nn.Linear(64, 512) # Linear projection layer for the query
        self.linear_k = torch.nn.Linear(64, 512) # Linear projection layer for the key
        self.linear_v = torch.nn.Linear(64, 512) # Linear projection layer for the value
        self.dropout_p = 0.2

    def forward(self, qk, x):
        scaled_qk = torch.nn.functional.linear(qk, weight=self.linear_q.weight, bias=self.linear_q.bias) \
                    / math.sqrt(self.linear_q.weight.shape[-1])  # Scale the dot product by the inverse scale factor
        softmax_qk = torch.nn.functional.softmax(scaled_qk, dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)  # Apply dropout to the softmax output
        output = torch.nn.functional.linear(dropout_qk, weight=self.linear_v.weight, bias=self.linear_v.bias) \
                 + torch.nn.functional.linear(x, weight=self.linear_k.weight, bias=self.linear_k.bias)  # Compute the dot product of the dropout output and the value
        return output
# Inputs to the model
qk = torch.randn(1, 64, 512)
x = torch.randn(1, 64, 512)
