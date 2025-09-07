
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(2048, 512) 
        self.key = torch.nn.Linear(2048, 512) 
        self.value = torch.nn.Linear(2048, 512)
 
    def forward(self, x):
        qk = torch.matmul(self.query(x), self.key(x).transpose(-2, -1))  # Compute the dot product of the query and key tensors
        scaled_qk = qk / 1000.0  # Scale the dot product by 1000
        softmax_qk = torch.nn.functional.softmax(scaled_qk)  # Apply softmax to the scaled dot product
        output = self.value(x).matmul(softmax_qk)  # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model
m = Model()
 
