
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_query = torch.nn.Linear(128, 16)
        self.linear_key = torch.nn.Linear(128, 16)
 
    def forward(self, x1, x2):
        qk = torch.matmul(self.linear_query(x1), self.linear_key(x2).transpose(-2, -1)) # Compute the dot product of the query and key tensors
        scaled_qk = qk / (1 / 0.5 ** 0.5) # Scale the dot product by the inverse scale factor
        softmax_qk = torch.nn.functional.softmax(scaled_qk, dim=-1) # Apply softmax to the scaled dot product
        output = softmax_qk.matmul(self.linear_value(x2))  # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(32, 128)
x2 = torch.randn(64, 128)
