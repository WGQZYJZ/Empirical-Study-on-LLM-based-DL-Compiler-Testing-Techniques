
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.att = torch.nn.Linear(d_model, d_head)
 
    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        scaled_qk = qk.mul(scale_factor)  # Scale the dot product by a factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        return self.att(dropout_qk).matmul(value)


# Initializing the model
m = Model()

