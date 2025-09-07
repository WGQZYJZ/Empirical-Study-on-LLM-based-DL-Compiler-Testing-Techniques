
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        k = self.conv(x1) / math.sqrt(x1.size(-1))
        k = k + x2.unsqueeze(0).unsqueeze(2)  # Add two tensors of shape [batch_size, channels, sequence_len, sequence_len] for the input to both query and key, as in this case it is not the input from the model
        k = torch.softmax(k, dim=-1)  # Compute softmax on all dimensions except the second dimension (the batch size)
        v = k @ x2  # Compute weighted sum of key * value
        return v


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
