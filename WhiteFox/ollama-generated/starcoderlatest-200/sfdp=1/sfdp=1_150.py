
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, query, key, value, inv_scale_factor, dropout_p):
        # TODO: Define the attention mechanism
        qk = torch.matmul(query, key.transpose(-2, -1)) / (inv_scale_factor * torch.tensor(10., dtype=torch.float32)) 
        softmax_qk = qk.softmax(-1) # Apply softmax to the scaled dot product of the query and key
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = dropout_qk.matmul(value) # Compute the dot product of the dropout output and the value tensor
        return output

# Inputs to the model
query = torch.randn(1, 3, 64, 64)
key = torch.randn(2, 3, 64, 64)
value = torch.randn(10, 3, 64, 64)
inv_scale_factor = torch.tensor(0.5, dtype=torch.float32).unsqueeze(-1).unsqueeze(-1) # TODO: Define the inverse scale factor
dropout_p = 0.5
