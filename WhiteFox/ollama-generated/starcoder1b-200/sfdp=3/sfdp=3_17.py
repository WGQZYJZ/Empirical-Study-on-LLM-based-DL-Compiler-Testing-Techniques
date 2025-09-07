
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query  = torch.nn.Linear(3, 64)  # Initialize a linear layer on the input
        self.key    = torch.nn.Linear(16, 8)  # Initialize a linear layer on the input
        self.value  = torch.nn.Linear(32, 8)  # Initialize a linear layer on the input
 
    def forward(self, x1):
        qk = self.query(x1).matmul(self.key.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        scaled_qk = qk.mul(scale_factor)  # Scale the dot product by a factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        output = dropout_qk.matmul(value)  # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model
m = Model()


