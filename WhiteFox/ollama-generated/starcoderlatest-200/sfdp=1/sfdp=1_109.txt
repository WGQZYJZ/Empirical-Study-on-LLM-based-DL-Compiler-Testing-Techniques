
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout_1 = torch.nn.Dropout2d(p=0.3)
 
    def forward(self, x1, x2, inv_scale_factor, query, key, value):
        qk  = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        scaled_qk = qk / (inv_scale_factor) # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p) # Apply dropout to the softmax output
        output = self.dropout_1(dropout_qk).matmul(value) # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model
m = Model()

