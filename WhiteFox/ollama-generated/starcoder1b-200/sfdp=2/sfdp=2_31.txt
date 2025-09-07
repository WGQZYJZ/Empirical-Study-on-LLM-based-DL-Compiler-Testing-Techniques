
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        qk = torch.matmul(x1, x2.transpose(-2, -1)) # Compute the dot product of the input tensors (the left operand and the right operand). Since the dimensions are different in the two cases, the batch dimension is always kept. So we use transpose to swap the batch dimension with the feature dimension (which is not necessarily `3`, but still 3 since we specify 1 stride and 1 padding in the convolution).
        scaled_qk = qk.div(inv_scale_factor) # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = dropout_qk.matmul(x3) # Compute the dot product of the dropout output and the value


# Initializing the model
m = Model()

# Inputs for training
input1  = torch.randn(4, 3, 64, 64) 
input2  = torch.randn(4, 3, 64, 64) 
