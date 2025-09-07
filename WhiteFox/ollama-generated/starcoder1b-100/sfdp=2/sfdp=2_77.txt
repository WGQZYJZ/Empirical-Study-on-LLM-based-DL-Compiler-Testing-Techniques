
class Model(torch.nn.Module):
    def __init__(self, input_size):
        super().__init__()
        self.fc1 = torch.nn.Linear(input_size, 16)
        self.fc2 = torch.nn.Linear(16, 32)
 
    def forward(self, x1):
        qk = torch.matmul(x1, x1.transpose(-2, -1))  # Compute the dot product of the query and the key
        scaled_qk = qk.div(math.sqrt(self.scale_factor))  # Scale the dot product by an inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        value = dropout_qk.matmul(x2)  # Compute the dot product of the dropout output and a value
        return output


# Initializing the model
m  = Model()


