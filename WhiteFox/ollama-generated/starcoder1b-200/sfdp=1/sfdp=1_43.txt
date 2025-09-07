
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.Linear(128, 32)
 
    def forward(self, x1):
        qk = torch.matmul(x1, x1.transpose(-2, -1)) # Compute the dot product of the input tensors
        inv_scale_factor = math.sqrt(64 / num_heads)  # Calculate the inverse scale factor for attention
        scaled_qk = qk.div(inv_scale_factor)  # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        output = dropout_qk.matmul(value)  # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model
m = Model()


