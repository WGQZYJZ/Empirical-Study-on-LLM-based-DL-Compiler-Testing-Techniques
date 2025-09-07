
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_q = torch.nn.Linear(768, 32)
        self.linear_k = torch.nn.Linear(768, 32)
        self.linear_v = torch.nn.Linear(768, 32)
 
    def forward(self, x1):
        qk = torch.matmul(x1, x1.transpose(-2, -1)) # Apply linear layer to input tensor x1
        qk = qk * scale_factor # Scale dot product by a factor
        softmax_qk = nn.functional.softmax(qk, dim=-1) # Apply softmax operation on the scaled dot product
        dropout_qk = nn.functional.dropout(softmax_qk, p=dropout_p) # Dropout
        output = torch.matmul(dropout_qk, x1) # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model
m = Model()


