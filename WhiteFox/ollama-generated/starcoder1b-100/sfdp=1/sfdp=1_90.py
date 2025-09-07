
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        query_tensor  = self.conv(x1)
        key_tensor   = self.conv(x2)
        scaled_query_tensor  = query_tensor  .div_(inv_scale_factor)  # Scale the dot product by the inverse scale factor
        softmax_query_tensor  = scaled_query_tensor.softmax(-1)  # Apply softmax to the scaled dot product
        dropout_query_tensor  = torch.nn.functional.dropout(softmax_query_tensor, p=dropout_p)  # Apply dropout to the softmax output
        output_tensor  = dropout_query_tensor.matmul(key_tensor)  # Compute the dot product of the dropout output and the key tensor
        return output_tensor


# Initializing the model
m  = Model()

