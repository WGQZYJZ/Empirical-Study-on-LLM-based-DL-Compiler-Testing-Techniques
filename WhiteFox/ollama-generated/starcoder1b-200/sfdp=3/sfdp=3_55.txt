
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Embedding(vocab_size, d)
        self.key = torch.nn.Linear(d, d)
        self.value = torch.nn.Linear(d, d)
 
        self.scale = 1
        self.softmax = 0
 
    def forward(self, x1, x2):
        qk = torch.matmul(x1, x2.transpose(-2, -1)) * self.scale  # Compute the dot product of the query and key tensors
        scaled_qk = qk.mul_(self.softmax)   # Scale the dot product by a factor
        dropout_qk = torch.nn.functional.dropout(scaled_qk, p=0.5)  # Apply dropout to the softmax output
        output = dropout_qk.matmul(x2)   # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model
m = Model()

