
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        qk = torch.matmul(x1, x2.transpose(-2, -1)) # Compute the dot product of the query and the key
        scale_factor = self.scale_factor  # The scale factor
        inv_scale_factor = 1 / scale_factor # The inverse of the scale factor
        softmax_qk = qk.div(inv_scale_factor) # Apply softmax to the scaled dot product
        drop = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        y1 = drop.matmul(value)  # Compute the dot product of the dropout output and the value
        return y1

# Initializing the model
m = Model()

