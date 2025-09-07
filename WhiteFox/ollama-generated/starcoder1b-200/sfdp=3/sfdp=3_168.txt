
class Model(torch.nn.Module):
    def __init__(self, model_dim):
        super().__init__()
        self.model_dim = model_dim
        self.linear1 = torch.nn.Linear(model_dim, 2*model_dim)
        self.tanh = torch.nn.Tanh()
        self.dropout = torch.nn.Dropout(dropout_p)
 
    def forward(self, x):
        qk = torch.matmul(x, x.transpose(-2, -1)) # Compute the dot product of the input and input transpose
        scaled_qk = qk.mul(scale_factor)  # Scale the dot product by a factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        output = dropout_qk.matmul(value) # Compute the dot product of the dropout output and the value tensor
        return self.linear1(output)


# Initializing the model
m = Model(model_dim=2*model_dim)

