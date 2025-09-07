
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(768, 32)
        self.key = torch.nn.Linear(768, 32)
        self.value = torch.nn.Linear(768, 32)
 
    def forward(self, x1):
        qk = torch.matmul(self.query(x1), self.key.transpose(-2, -1)) # Compute the dot product of the query and the key
        scaled_qk = qk / (0.007843 + 0.00784) # Scale the dot product by the inverse scale factor
        softmax_qk = torch.nn.functional.softmax(scaled_qk, dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = dropout_qk * self.value(x1) # Compute the dot product of the dropout output and the value
        return output


# Inputs to the model
x1 = torch.randn(2, 3, 768)
