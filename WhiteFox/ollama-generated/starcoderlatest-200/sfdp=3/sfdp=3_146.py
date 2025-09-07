
class AttentionModel(torch.nn.Module):
    def __init__(self, key_length=256, query_length=768):
        super().__init__()
        self.key_projection = torch.nn.Conv1d(query_length, key_length, 1)
        self.value_projection = torch.nn.Conv1d(query_length, query_length, 1)
 
    def forward(self, q):
        v = self.value_projection(q).unsqueeze(-2) # Add an extra dimension to the output of the convolution
        k = self.key_projection(q).unsqueeze(-3)
        scaled_qk = torch.matmul(k, v) * scale_factor
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        return torch.matmul(dropout_qk, v), softmax_qk # Return the result of matrix multiplication and apply a linear transformation

# Inputs to the model
q1 = torch.randn(8, 256, 768).unsqueeze(-3)
m1, __softmax_qk__ = m(q1)

