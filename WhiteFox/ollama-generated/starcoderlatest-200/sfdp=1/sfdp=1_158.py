
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2, query, key, value):
        scaled_qk = torch.matmul(query, key.transpose(-2, -1)) # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        return (torch.matmul(dropout_qk, value))
 

# Input data:
query = torch.randn(1, 32, 64, 64)
key = torch.randn(1, 32, 64, 64)
value = torch.randn(1, 32, 64, 64)


