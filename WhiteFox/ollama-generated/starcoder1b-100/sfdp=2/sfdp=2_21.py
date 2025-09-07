
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query  = torch.nn.Linear(10, 8)
        self.key    = torch.nn.Linear(8, 6)
        self.value  = torch.nn.Linear(6, 1)
 
    def forward(self, x):
        qk = torch.matmul(self.query(x), self.key(x).transpose(-2, -1))  # Compute the dot product of the query and the key
        scaled_qk = qk.div(torch.sqrt(self.key(x).size(-1) / self.value(x).size(-1)))  # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        value = self.value(x).unsqueeze(2).expand_as(x)  # Expand the batch dimension and apply to all elements of the output tensor
        return dropout_qk.matmul(value)


# Initializing the model
m = Model()


