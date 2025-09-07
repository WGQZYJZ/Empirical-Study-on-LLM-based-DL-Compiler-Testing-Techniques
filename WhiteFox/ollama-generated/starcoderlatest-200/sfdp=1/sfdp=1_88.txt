
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.q = torch.nn.Linear(1024, 1024)
        self.k = torch.nn.Linear(1024, 1024)
        self.v = torch.nn.Linear(1024, 1024)
 
    def forward(self, x):
        q = self.q(x).unsqueeze(-2) # Unsqueeze the last dimension so it matches query shape
        k = self.k(x).unsqueeze(-3) # Unsqueeze the third dimension so it matches key shape
        v = self.v(x).unsqueeze(-1) # Unsqueeze the second dimension so it matches value shape
        qk = torch.matmul(q, k.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        scaled_qk = qk.div(inv_scale_factor)  # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        output = dropout_qk.matmul(v)  # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 2048, 1536, 768)
