
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(768, 512)
        self.key = torch.nn.Linear(512, 512)
        self.value = torch.nn.Linear(512, 512)
        self.dropout = torch.nn.Dropout(0.25)
 
    def forward(self, x1):
        query = self.query(x1).transpose(-2, -1)  # Compute the dot product of the query and key tensors
        key = self.key(x1)
        value = self.value(x1)
        dropout_qk = torch.nn.functional.dropout(
            torch.matmul(query, key), p=self.dropout.p)  # Apply dropout to the softmax output
        return torch.matmul(dropout_qk, value)


# Initializing the model
m = Model()


