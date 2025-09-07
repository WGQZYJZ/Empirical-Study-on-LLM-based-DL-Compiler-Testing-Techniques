
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(4, 3)
        self.key   = torch.nn.Linear(2, 3)
        self.value = torch.nn.Linear(2, 5)
 
    def forward(self, x1, x2):
        qk = torch.matmul(self.query(x1), self.key(x2).transpose(-2, -1)) # Compute the dot product of the query and the key
        scale_factor = 1/np.sqrt(self.value.weight.detach().numpy()[0])
        softmax_qk = qk / np.sqrt(scale_factor) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        return self.value(dropout_qk.matmul(self.value.weight))


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(4, 3)
x2  = torch.randn(2, 3)
