
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention()
 
    def forward(self, query, key, value):
        qk  = torch.matmul(query, key.transpose(-2, -1)) 
        scaled_qk = qk.div(inv_scale_factor) # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output  = dropout_qk.matmul(value) # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
key = torch.randn(8, 3, 32, 32) # The query tensor should be generated with a dimension of (8, 3, H/32, W/32), where H and W are the height and width of each image in pixels
value = torch.randn(16, 3, 32, 32) # The value tensor should be generated with a dimension of (16, 3, H/32, W/32), where H and W are the height and width of each image in pixels
