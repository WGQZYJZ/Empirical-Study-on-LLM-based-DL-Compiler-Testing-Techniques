
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.att  = torch.nn.Linear(768, 3072)
        self.fc   = torch.nn.Linear(3072, 1024)
 
    def forward(self, x1):
        qk = torch.matmul(x1, x1.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        scaled_qk = qk.div(inv_scale_factor) # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = self.att(dropout_qk) + self.fc(x1) # Compute the weighted sum of the attention mechanism and linear layers
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 768, 128, 128)
