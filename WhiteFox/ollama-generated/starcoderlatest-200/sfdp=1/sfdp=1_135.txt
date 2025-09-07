
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(2048, 16384) # Number of hidden units is set to 16384 because the number of features is set to 2048 and the query dimension is 1920
        self.key = torch.nn.Linear(512, 16384)

    def forward(self, x):
        v1 = self.query(x).unsqueeze(-1).repeat([1, 1, x.size()[2], x.size()[3]]) # Expand the query dimension from [1920] to [B, L, H, W]. Repeat along the length axis 4 times to get [B, L, H, W, 16384]
        v2 = self.key(x).unsqueeze(-2).repeat([1, 1, x.size()[1], x.size()[2]]) # Expand the key dimension from [1920] to [B, D, H, W]. Repeat along the channel axis 4 times to get [B, D, H, W, 512]
        qk = torch.matmul(v1, v2) # Compute the dot product of the query and key tensors
        scaled_qk = qk.div(inv_scale_factor) # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = dropout_qk.matmul(self.value).transpose(-2,-1) # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model
m = Model()

# Inputs to the model
x  = torch.randn(3, 512, 10, 16)
