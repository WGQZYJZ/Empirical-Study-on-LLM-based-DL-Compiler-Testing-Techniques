
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.softmax = torch.nn.Softmax(dim=-1)
        self.matmul_1 = torch.nn.Linear(2048, 512)

    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        scaled_qk = qk.div(inv_scale_factor) # Scale the dot product by the inverse scale factor
        softmax_qk = self.softmax(scaled_qk) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = self.matmul_1(dropout_qk).transpose(-2, -1).contiguous()
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(8, 2048, 76, 76)
