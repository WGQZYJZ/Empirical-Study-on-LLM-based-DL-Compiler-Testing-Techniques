
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(10, 256)
        self.key = torch.nn.Linear(256, 384)
        self.value = torch.nn.Linear(384, 512)
 
    def forward(self, x1):
        qk = torch.matmul(x1, self.query)  # Compute the dot product of the query and key tensors
        scaled_qk = qk / math.sqrt(math.pow(self.key.weight.size(0), -0.5)) # Scale the dot product by an inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)  # Apply dropout to the softmax output
        return self.value.matmul(dropout_qk)


# Initializing the model
m = Model()


