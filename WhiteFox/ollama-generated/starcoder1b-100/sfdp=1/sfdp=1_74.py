
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(5, 3)
        self.key = torch.nn.Linear(7, 4)
 
    def forward(self, x1, x2):
        qk = torch.matmul(x1, x2.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        scale_factor = torch.inverse(torch.sqrt(qk + 1e-6))  # Calculate the inverse sqrt of the scaled dot product
        softmax_qk = qk / scale_factor  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        return dropout_qk.matmul(x3)  # Compute the dot product of the dropout output and the value tensor


# Initializing the model
m = Model()


