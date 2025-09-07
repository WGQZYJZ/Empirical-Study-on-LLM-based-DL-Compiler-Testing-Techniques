
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        query  = torch.randn(1, 64, 1, 1, dtype=torch.float64) # Generate a random query tensor
        key     = torch.randn(8, 64, 3, 3, dtype=torch.float64) # Generate a random key tensor
        scaled_qk = torch.matmul(query, key.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        inv_scale_factor = torch.pow(scaled_qk.shape[0], -0.5)  # The inverse scale factor is used to prevent log from exploding
        scaled_softmax_qk = scaled_qk.div(inv_scale_factor)  # Scale the dot product by the inverse scale factor
        dropout_qk = torch.nn.functional.dropout(scaled_softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        value = dropout_qk.matmul(x2) # Compute the dot product of the dropout output and the value tensor

# Initializing the model
m = Model()

