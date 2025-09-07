
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        query = torch.randn((4, 8, 64, 64))  # Generate a random query tensor of size (batch_size, input_channels, sequence_length, sequence_length).
        key = torch.randn((2, 8, 64, 64))  # Generate a random key tensor of size (batch_size, output_channels, sequence_length, sequence_length).
        query_norm = (query / math.sqrt(query.shape[-1])).permute(0, 2, 3, 1)  # Normalize the query to its batch-first representation.
        key_norm = (key / math.sqrt(key.shape[-1])).permute(0, 2, 3, 1)  # Normalize the key to its batch-first representation.
        scaled_qk = torch.matmul(query_norm, key_norm)  # Compute the dot product of the query and key tensors
        dropout_qk = torch.nn.functional.dropout(scaled_qk, p=dropout_p)  # Apply dropout to the softmax output
        v  = dropout_qk.matmul(value)  # Compute the dot product of the dropout output and the value tensor
        return v


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(3, 8, 64, 64)
