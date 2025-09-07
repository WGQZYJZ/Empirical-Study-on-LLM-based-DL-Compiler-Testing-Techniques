
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        query = x1.reshape((x1.shape[0], -1))  # Reshape the input tensor to flatten a single dimension
        key   = x2.reshape((x2.shape[0], -1))
        v    = self.conv(query)  # Apply convolution on both sides
        v    = torch.nn.functional.dropout(v, p=dropout_p)  # Apply dropout on the input tensor
        v    = v.matmul(key.transpose(-2, -1))  # Multiply the output by the input and key tensors
        scale_factor  = torch.sqrt(torch.mm(v, v.t()))  # Compute the square root of the dot product
        softmax_factor = scaled_qk.softmax(dim=-1)  # Apply softmax on both sides
        dropout_factor = torch.nn.functional.dropout(softmax_factor, p=dropout_p)  # Apply dropout to both sides
        output = dropout_factor.matmul(value)  # Compute the dot product of the two dropout factors and the value tensor
        return output


# Initializing the model
m = Model()

