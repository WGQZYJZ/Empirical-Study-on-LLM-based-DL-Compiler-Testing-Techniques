
class Model(torch.nn.Module):
    def __init__(self, dropout_p):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
        self.dropout = torch.nn.Dropout(dropout_p)
 
    def forward(self, x1, x2):
        qk  = torch.matmul(x1, x2.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        scaled_qk = qk.div(inv_scale_factor)  # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        output = self.dropout(softmax_qk).matmul(x2)  # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model
m = Model()

