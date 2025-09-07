
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(768, 1024)
        self.key = torch.nn.Linear(1024, 1024)
        self.value = torch.nn.Linear(1024, 512)
        self.dropout_p = 0.1

    def forward(self, x1):
        qk = torch.matmul(x1, self.key.weight.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        v = torch.matmul(qk, self.value.weight) # Compute the dot product of the dropout output and the value tensor
        drop_out = torch.nn.functional.dropout(v, p=self.dropout_p)  # Apply dropout to the softmax output
        output = self.query.weight.matmul(drop_out)  # Compute the dot product of the query weights and the dropout output
        return output

# Initializing the model
m = Model()


