
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1  = torch.nn.Linear(20, 4)
 
    def forward(self, x):
        qk = torch.matmul(x, self.linear1(x).transpose(-2, -1)) # Compute the dot product of a query and a key 
        scaled_qk = qk / inv_scale_factor  # Scale the dot product by an inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1)   # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output 
        return dropout_qk.matmul(self.linear2(x))

# Initializing the model
m  = Model()

