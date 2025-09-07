
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(8, 16)
        self.key = torch.nn.Linear(8, 16)
        self.value = torch.nn.Linear(8, 16)
        self.dropout = nn.Dropout(p=0.25)
 
    def forward(self, x1):
        qk = torch.matmul(x1, self.key.transpose(-2, -1))
        scaled_qk = qk.div(torch.rsqrt(q.size(-1)))  # Compute the dot product of the query and key tensors
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        output = self.dropout(softmax_qk).matmul(self.value)  # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model
m = Model()


