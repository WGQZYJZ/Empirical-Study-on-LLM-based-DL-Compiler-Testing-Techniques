
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query_proj = torch.nn.Linear(2048, 16)
        self.key_proj   = torch.nn.Linear(2048, 16)

    def forward(self, x1, x2):
        qk = torch.matmul(self.query_proj(x1), self.key_proj(x2).transpose(-2,-1)) # Apply linear layers to compute the dot product of query and key tensors
        scaled_qk = qk * scale_factor 
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = dropout_qk.matmul(self.value_proj(x2)) # Compute the dot product of the dropout output and the value tensor
        return output
