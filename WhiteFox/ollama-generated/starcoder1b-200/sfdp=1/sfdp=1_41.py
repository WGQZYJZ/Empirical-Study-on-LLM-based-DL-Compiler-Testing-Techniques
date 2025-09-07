
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_query = torch.nn.Linear(d1, d2)  # Linear layer with d1 inputs and d2 outputs
        self.linear_key = torch.nn.Linear(d2, d3)  # Linear layer with d2 inputs and d3 outputs
        self.linear_value = torch.nn.Linear(d3, d4)  # Linear layer with d3 inputs and d4 outputs
        self.dropout = torch.nn.functional.dropout  # Dropout layer with dropout probability p=0.1
    
    def forward(self, x1, x2):
        qk = torch.matmul(x1, x2.transpose(-2, -1))
        scaled_qk = qk / math.sqrt(d3)
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = self.dropout(softmax_qk, p=0.1)  # Apply dropout to the softmax output
        y = dropout_qk.matmul(self.linear_value(x2))  # Compute the dot product of the dropout output and the value tensor
        return torch.tanh(self.linear_query(x1)) + y


# Initializing the model
m = Model()


