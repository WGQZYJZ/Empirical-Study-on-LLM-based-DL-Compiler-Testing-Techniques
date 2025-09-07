
class Model(torch.nn.Module):
    def __init__(self, d_k, d_v, nhead=8, qkv_bias=False):
        super().__init__()
        self.qkv = torch.nn.Linear(d_k, 3 * d_k, bias=qkv_bias)
        self.scale_factor = torch.nn.Parameter(torch.ones(1), requires_grad=True)
        self.dropout = torch.nn.Dropout(p=0.5)

    def forward(self, x):
        query = self.qkv(x).contiguous().view(-1, 3 * self.scale_factor.size(0), 2, d_k // 2)  # (batch size x seq len x features in key)
        scaled_query = query.mul(self.scale_factor)  # Scale the dot product by a factor
        dropout_query = torch.nn.functional.dropout(scaled_query, p=0.5)  # Apply dropout to the softmax output
        value = self.qkv(x).contiguous().view(-1, 3 * self.scale_factor.size(0), d_k // 2)  # (batch size x seq len x features in key)
        scaled_value = value.mul(self.scale_factor)  # Scale the dot product by a factor
        dropout_value = torch.nn.functional.dropout(scaled_value, p=0.5)  # Apply dropout to the softmax output
        attention = dropout_query.matmul(dropout_value)  # Compute the dot product of the dropout output and the value tensor
        output = self.dropout(attention)  # Apply dropout to the output
        return output


# Initializing the model
m = Model(d_k=32, d_v=16, qkv_bias=True)


