
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(3072, 10)
        self.key = torch.nn.Linear(3072, 8)
        self.value = torch.nn.Linear(3072, 4)
        self.dropout_p = 0.5

    def forward(self, x):
        # Get the query and key from their respective layers
        q = self.query(x).view(-1, self.key.weight.size(-1))
        k = self.key(x).view(-1, self.value.weight.size(-1))
        v = self.value(x).view(-1, self.value.weight.size(-1))

        # Compute the scaled dot product
        qk = torch.matmul(q, k.transpose(-2, -1))  # [B, Q_len * K_len]
        scaled_qk = qk.mul(self.scale_factor)  # Scale the dot product by a factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)

        # Compute the output tensor from the scaled and dropouted tensors
        return dropout_qk.matmul(v)


# Inputs to the model
x = torch.randn(1, 3072, requires_grad=True)
output = Model()(x)
