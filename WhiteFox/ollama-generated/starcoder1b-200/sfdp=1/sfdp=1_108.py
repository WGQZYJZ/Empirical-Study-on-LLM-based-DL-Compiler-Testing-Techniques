
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query_conv = torch.nn.Conv2d(10, 16, 1)
        self.key_conv = torch.nn.Conv2d(16, 32, 1)
        self.value_conv = torch.nn.Conv2d(32, 64, 1)
 
    def forward(self, x):
        vq = self.query_conv(x)  # Compute the dot product of the query and key tensors
        vk = self.key_conv(x)  # Compute the dot product of the query and key tensors
        vw = self.value_conv(x)  # Compute the dot product of the query and key tensors
        output = torch.nn.functional.relu(vq + vk)  # Apply relu to the dot product of the query and key tensors
        # Apply dropout on the output from the relu operation
        d_output, _ = torch.chunk(output, chunks=2, dim=-1)  # Unfold the last two dimensions of output (i.e., [batch size, hidden size])
        d_output = torch.nn.functional.dropout(d_output, p=dropout_p)  # Apply dropout on the unfolded output
        d_output, _ = torch.chunk(d_output, chunks=1, dim=-2)  # Unfold the last dimension of the second output (i.e., [batch size, hidden size])
        return d_output  # Return the unfolded output


# Initializing the model
m = Model()


