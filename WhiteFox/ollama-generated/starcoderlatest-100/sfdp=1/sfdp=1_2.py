
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.key   = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x):
        qk = torch.matmul(self.query(x), self.key.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        scaled_qk = qk / math.sqrt(x.shape[-1]) # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        output = torch.nn.functional.dropout(softmax_qk, p=0.5) # Apply dropout to the softmax output
        return output

# Initializing the model
m = Model()

# Inputs to the model
x  = torch.randn(1, 3, 64, 64)
