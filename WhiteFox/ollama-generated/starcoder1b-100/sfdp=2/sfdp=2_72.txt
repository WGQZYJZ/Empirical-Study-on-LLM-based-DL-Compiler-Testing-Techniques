
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(d_model, d_model)
        self.key   = torch.nn.Linear(d_model, d_model)
        self.value = torch.nn.Linear(d_model, d_model)
 
    def forward(self, x1):
        qk  = torch.matmul(x1, self.key.weight)  # Compute the dot product of the query and the key
        s_qk = qk.div(self.scaling_factor).softmax()  # Scale the dot product by an inverse scale factor
        dropout_qk = torch.nn.functional.dropout(s_qk, p=0.1)  # Apply dropout to the softmax output
        v = self.value(dropout_qk)  # Compute the dot product of the dropout output and the value
        return v

# Initializing the model
m = Model()


